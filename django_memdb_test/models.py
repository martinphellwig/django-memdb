from django.db import models

from django_memdb.mixins import InMemoryDB, PeristentInMemoryDB
# Create your models here.

class TestModelWithMixin(models.Model, InMemoryDB):
    text = models.TextField()

class TestModelPersistent(models.Model, PeristentInMemoryDB):
    text = models.TextField()
