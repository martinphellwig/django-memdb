"""
This are the signals this app emits.
"""
from django import dispatch

# pylint: disable=invalid-name

store_save = dispatch.Signal(providing_args=['kwargs'])
store_load = dispatch.Signal(providing_args=['kwargs'])
