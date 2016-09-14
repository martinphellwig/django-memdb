"""
Processors for storing the in-memdb persistently.
"""
import json
from io import StringIO

from django.core.management import call_command
from django.conf import settings

from .mixins import PeristentInMemoryDB
from .models import PersistentStorage
from . import settings
from . import signals

# pylint: disable=unused-argument, no-member
def callback(*args, **kwargs):
    "Callback used for hooking in to memory models save."
    if not issubclass(kwargs['sender'], PeristentInMemoryDB):
        return

    if not settings.MEMDB_RESTORED: # pragma: no cover
        return

    # pylint: disable=protected-access
    application = kwargs['sender']._meta.app_label
    model = kwargs['sender'].__name__

    string_io = StringIO()
    call_command('dumpdata', application + '.' + model,
                 '--database', settings.MEMDB_NAME, stdout=string_io)
    data = string_io.getvalue()
    # The database dump contains brackets on each end, even when empty.
    if len(data) <= 2:
        # So empty table, means we can remove all entries for it in the db.
        PersistentStorage.objects.all().delete()
        return

    arguments = {'data':json.loads(data),
                 'application':application,
                 'model':model,
                 'database':settings.MEMDB_NAME,
                 'processors':[],
                 'process': settings.MEMDB_PROCESS_ENCODE}
    signals.store_save.send(object, kwargs=arguments)

    for processor in arguments['processors']:
        processor(arguments)

    journal = PersistentStorage()
    journal.application = arguments['application']
    journal.modelname = arguments['model']
    journal.codec = str(arguments['processors'])
    journal.data = json.dumps(arguments['data'])
    journal.save()

    # remove previous entries.
    to_delete = PersistentStorage.objects.filter(application=application, modelname=model)
    to_delete = to_delete.exclude(inserted=journal.inserted)
    to_delete.delete()
