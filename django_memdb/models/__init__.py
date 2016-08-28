"""
Django MemDB, ironically, journals to a default database.
"""
from django.db import models

# Create your models here.
class Journal(models.Model):
    """Stores the data of the in-memory database.
    This means we can recreate the in-memory database on restart.
    """
    application = models.CharField(max_length=63)
    inserted = models.DateTimeField(auto_now_add=True)
    codec = models.CharField(max_length=128)
    data = models.TextField()
