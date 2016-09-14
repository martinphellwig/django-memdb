"""
This module is imported on app ready (see __init__).
"""
from django.db.models import signals as dms
import django_query_signals as dqs

from .processors import callback

dms.post_save.connect(callback)
dms.post_delete.connect(callback)
dqs.post_bulk_create.connect(callback)
dqs.post_delete.connect(callback)
dqs.post_get_or_create.connect(callback)
dqs.post_update.connect(callback)
dqs.post_update_or_create.connect(callback)
