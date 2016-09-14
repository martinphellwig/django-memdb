"Restore the in memory data."
import json
from django.db.utils import OperationalError
from django.core import serializers
from ..models import PersistentStorage
from .. import settings
from .. import signals

def restore(query=None):
    "restore persistent in-mem tables."
    settings.MEMDB_RESTORED = True
    if query is None:
        # pylint: disable=no-member
        try:
            query = PersistentStorage.objects.all()
            query.count()
        except OperationalError: # pragma: no cover
            return

    for instance in query:
        arguments = {'data':instance.data,
                     'application':instance.application,
                     'model':instance.modelname,
                     'database':settings.MEMDB_NAME,
                     'processors':[],
                     'process': settings.MEMDB_PROCESS_DECODE}

        signals.store_load.send(object, kwargs=arguments)

        for processor in arguments['processors']:
            processor(arguments)

        if isinstance(arguments['data'], bytes):
            arguments['data'] = arguments['data'].decode('utf-8')

        if isinstance(arguments['data'], str):
            try:
                arguments['data'] = json.loads(arguments['data'])
            except json.JSONDecodeError:
                pass

        objects = serializers.deserialize('json', json.dumps(arguments['data']))
        for obj in objects:
            obj.save()
