.. image:: https://img.shields.io/codeship/a9873030-5c43-0134-5e91-46e8172ca5a4/default.svg
   :target: https://bitbucket.org/hellwig/django-memdb
.. image:: https://coveralls.io/repos/bitbucket/hellwig/django-memdb/badge.svg?branch=default 
   :target: https://coveralls.io/bitbucket/hellwig/django-memdb?branch=default
.. image:: https://img.shields.io/pypi/v/django-memdb.svg
   :target: https://pypi.python.org/pypi/Django-MemDB/
.. image:: https://img.shields.io/badge/Donate-PayPal-blue.svg
   :target: https://paypal.me/MartinHellwig
.. image:: https://img.shields.io/badge/Donate-Patreon-orange.svg
   :target: https://www.patreon.com/hellwig
   

######################
Django Memory Database
######################

What is it?
===========
A library that allows tables to be kept in an in-memory database and optionally
can provide persistence between instance restart by spooling the tables to a
table that is read upon startup to populate the in-memory tables.  

What problem does it solve?
===========================
Create in-memory tables with optional data persistence. 

How do I install it?
====================
.. sourcecode:: shell

  pip install django-memdb


Adding to Django (using integrator)
-----------------------------------
.. sourcecode:: python

  # At the bottom of your settings.py file.
  import django_integrator
  django_integrator.add_application('django_memdb')

If you don't want to use the above, add the application to INSTALLED_APPS and
merge the apps settings.py and url.py into the django projects files. 

How do I use it?
================
When defining models, use the class mixin.

For example:

.. sourcecode:: python

  from django.db import models
  from django_memdb.mixins import InMemoryDB, PeristentInMemoryDB
  
  class TestModelWithMixin(models.Model, InMemoryDB):
      text = models.TextField()
  
  class TestModelPersistent(models.Model, PeristentInMemoryDB):
      text = models.TextField()


Both mixins work more like a tag, which is used to determine if a table is an
in-memory table or not and if the table contents should be stored in the
(using the default database) PersistentStorage model.

You can optionally hook into the persistentstorage mechanics by attaching to the
signals this app provides. The below example will add compression the data
before storing it:

.. sourcecode:: python

	from django_memdb import signals
	
	def compress(arguments):
	    "Compress data."
	    # pylint: disable=redefined-variable-type
	    if arguments['process'] == settings.MEMDB_PROCESS_ENCODE:
	        data = arguments['data']
	        data = json.dumps(data)
	        data = data.encode('utf-8')
	        data = zlib.compress(data)
	        arguments['data'] = data
	    elif arguments['process'] == settings.MEMDB_PROCESS_DECODE:
	        data = arguments['data']
	        data = zlib.decompress(data)
	        data = data.decode('utf-8')
	        data = json.loads(data)
	        arguments['data'] = data
	
	def callback(sender, **kwargs): # pylint: disable=unused-argument
	    "Just insert a hook."
	    kwargs['kwargs']['processors'].append(compress)
	
	
	signals.store_save.connect(callback)
	signals.store_load.connect(callback)


Caveat
======
The in memory database is local to each server instance, thus if you have a
setup that uses multiple servers and a single django database instance, you will
have synchronisation issues with the in-memory data and hard conflicts when
using the persistent storage.

What license is this?
=====================
Two-clause BSD


How can I get support?
======================
Please use the repo's bug tracker to leave behind any questions, feedback,
suggestions and comments. I will handle them depending on my time and what looks
interesting. If you require guaranteed support please contact me via
e-mail so we can discuss appropriate compensation.


Signing Off
===========
Is my work helpful or valuable to you? You can repay me by donating via:

https://paypal.me/MartinHellwig

.. image:: https://img.shields.io/badge/PayPal-MartinHellwig-blue.svg
  :target: https://paypal.me/MartinHellwig
  :alt: Donate via PayPal.Me
  :scale: 120 %

-or-

https://www.patreon.com/hellwig

.. image:: https://img.shields.io/badge/Patreon-hellwig-orange.svg
  :target: https://www.patreon.com/hellwig
  :alt: Donate via Patreon
  :scale: 120 %


Thank you!