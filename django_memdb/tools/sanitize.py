"""
Perform sanitization check prior of releasing the app as ready.
"""
from io import StringIO
from django.conf import settings
from django.core.management import call_command

def main():
    "Perform sanitization checks"
    dbs = '--database=%s' % settings.MEMDB_NAME
    stdout = StringIO()
    call_command('migrate', dbs, stdout=stdout)
