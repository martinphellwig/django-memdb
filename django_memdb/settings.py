"""
This projects settings.
"""
# These settings can be imported with the django_app_importer tool
URLCONF = 'urls'

MEMDB_NAME = 'django_memdb'

DATABASES = {
    MEMDB_NAME: {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'file::memory:?cache=shared'}
}

DATABASE_ROUTERS = ['django_memdb.dbrouter.MemDB']
