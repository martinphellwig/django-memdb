"""
This projects settings.
"""
# These settings can be imported with the django_app_importer tool
INSTALLED_APPS = ['django_query_signals']

MEMDB_NAME = 'django_memdb'

DATABASES = {
    MEMDB_NAME: {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'file::memory:?cache=shared'}
}

DATABASE_ROUTERS = ['django_memdb.dbrouter.MemDB']

MEMDB_RESTORED = False
MEMDB_PROCESS_ENCODE = 'encode'
MEMDB_PROCESS_DECODE = 'decode'
