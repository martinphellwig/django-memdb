"""
Perform sanitization check prior of releasing the app as ready.
"""

from django.conf import settings
from django.core.management import call_command

def main():
    "Perform sanitization checks"
    dbs = '--database=%s' % settings.MEMDB_NAME
    call_command('migrate', dbs)
