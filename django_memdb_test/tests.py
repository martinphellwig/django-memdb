if __name__ == '__main__':
    import django
    django.setup()

from django.test import TestCase
from django_memdb_test.models import TestModelWithMixin


class MainTest(TestCase):
    def test_01_smoke(self):
        TestModelWithMixin.objects.create(text='some text')
        x = TestModelWithMixin.objects.all()
        print(x)


if __name__ == '__main__':
    from django.core.management import call_command
    call_command('test')