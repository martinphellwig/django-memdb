"Test module"
import zlib
import json

from django.test import TestCase
from django_memdb import settings
from django_memdb.models import PersistentStorage
from django_memdb.tools import restore
from django_memdb import signals
from django_memdb_test.models import TestModelWithMixin, TestModelPersistent

def extra_process(arguments):
    "Testing extra handling."
    # pylint: disable=redefined-variable-type
    if arguments['process'] == settings.MEMDB_PROCESS_ENCODE:
        data = arguments['data']
        data = json.dumps(data)
        data = data.encode('utf-8')
        data = zlib.compress(data)
        arguments['data'] = data
    elif arguments['process'] == settings.MEMDB_PROCESS_DECODE:
        data = arguments['data']
        data = zlib.decompress(data)
        data = data.decode('utf-8')
        data = json.loads(data)
        arguments['data'] = data

def hook(sender, **kwargs): # pylint: disable=unused-argument
    "Just insert a hook."
    kwargs['kwargs']['processors'].append(extra_process)

#pylint: disable=no-member
class MainTest(TestCase):
    "The main test case"
    def test_01_smoke(self):
        "smoke test"
        TestModelWithMixin.objects.create(text='some text')
        query = TestModelWithMixin.objects.all()
        self.assertEqual(query.count(), 1)
        query.delete()
        self.assertEqual(query.count(), 0)

    def test_02_bulk_create(self):
        "can we bulk create and still catch the signal."
        count = TestModelPersistent.objects.all().count()
        TestModelPersistent.objects.bulk_create(
                                           [TestModelPersistent(text='yeah!'),])
        query = TestModelPersistent.objects.all()
        self.assertEqual(query.count(), count+1)

    def test_03_create(self):
        "can we create a model direct and still catch it."
        count = TestModelPersistent.objects.all().count()
        instance = TestModelPersistent()
        instance.text = 'yeah!'
        instance.save()
        query = TestModelPersistent.objects.all()
        self.assertEqual(query.count(), count+1)

    def test_04_bulk_delete(self):
        "If we create a bunch, and delete it, will the journal item be deleted?"
        self.test_02_bulk_create()
        self.test_02_bulk_create()
        self.test_02_bulk_create()
        query = PersistentStorage.objects.all()
        self.assertEqual(query.count(), 1)
        TestModelPersistent.objects.all().delete()
        query = PersistentStorage.objects.all()
        self.assertEqual(query.count(), 0)

    def test_06_restore(self):
        "Can we restore an item by simulating a system startup."
        signals.store_save.connect(hook)
        signals.store_load.connect(hook)
        self.test_02_bulk_create()
        got = PersistentStorage.objects.all()
        query = list(got)

        got.delete()
        self.assertFalse(PersistentStorage.objects.all().exists())
        settings.MEMDB_RESTORED = False
        restore.restore(query)
        self.assertTrue(PersistentStorage.objects.all().exists())
        self.assertTrue(settings.MEMDB_RESTORED)
