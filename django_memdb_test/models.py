from django.db import models

from django_memdb.mixins import InMemoryDB
# Create your models here.

class TestModelWithMixin(models.Model, InMemoryDB):
    text = models.TextField()