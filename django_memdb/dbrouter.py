'''
Created on 11 Aug 2016

@author: martin
'''
from django.conf import settings
from . import mixins

INMEMDB = settings.MEMDB_NAME

# pylint: disable=no-self-use, unused-argument, invalid-name
class MemDB(object):
    "Database router for Memory Database"
    def __init__(self):
        self.db_for_read = self._db_for_rw
        self.db_for_write = self._db_for_rw

    def _db_for_rw(self, model, **hints):
        "Return database to use for read/write."
        if issubclass(model, mixins.InMemoryDB):
            return INMEMDB

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Allow migrations for 'model_name' on 'db'?
        """
        in_mem = False
        if 'model' in hints:
            if issubclass(hints['model'], mixins.InMemoryDB):
                in_mem = True

        if db == INMEMDB:
            returns = in_mem
        else:
            returns = not in_mem

        return returns

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations
        """
        return None # pragma: no cover
