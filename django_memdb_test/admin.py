"""
Default admin interface setup.
"""
from django.contrib import admin
from . import models

admin.site.register(models.TestModelWithMixin)
admin.site.register(models.TestModelPersistent)
