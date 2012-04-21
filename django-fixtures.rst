Fixtures
========

When the django project and its applications are installed on a new machine,
the initial state of the database will be empty. You can use `fixtures
<https://docs.djangoproject.com/en/1.4/howto/initial-data/>`_ to automatically
load data into the database when you run syncdb. This is especially useful for
unit testing which we will go into detail on shortly.

First let's make a fixture for our doodle model. To make a fixture, you need to
prepare some data. One avenue for doing this is to manually create some model
instances as we have done in :doc:`django-create-model`, and then dump them out
of the database into a format such as yaml, json or xml. First create a
directory in which to store the glable fixtures (like our users list) and 
and application specific fixture for doodle data data::
   
   mkdir -p doodle_app/fixtures

Now dump the database data into json text files::
   
   python manage.py dumpdata --indent=4 doodle_app  > doodle_app/fixtures/initial_data.json

.. note:: (1) You must call the fixture **initial_data.json|yaml|xml** if you
   want it to load automatically when running syncdb (and it will load every time
   you run syncdb!). 
   (2) You can create other fixtures to use in specific contexts like a 
   particular unit test - which we will see later.
   (3) The ``--indent=4`` options makes the fixture file size bigger but the
   contents easier to read.
   (4) If your fixtures are very large, it will probably be more efficient
   to do a database dump and restore. Fixtures are handy for populating lookup
   tables and for installing a small amount of data for unit testing.

To test our fixture is working, we can remove our :file:`django.db` and then
recreate it using :command:`syncdb` - our 3 doodles should be reinstated::
   
  $ rm django.db; python manage.py syncdb
  Creating tables ...
  Creating table auth_permission
  Creating table auth_group_permissions
  Creating table auth_group
  Creating table auth_user_user_permissions
  Creating table auth_user_groups
  Creating table auth_user
  Creating table django_content_type
  Creating table django_session
  Creating table django_site
  Creating table doodle_app_doodle

  You just installed Django's auth system, which means you don't have any superusers defined.
  Would you like to create one now? (yes/no): no
  Installing custom SQL ...
  Installing indexes ...
  Installed 3 object(s) from 1 fixture(s)


For now we will remove our :file:`initial_data.json` fixture as it is mostly
useful with lookup tables, which we haven't created yet!::
   
  rm doodle_app/fixtures/initial_data.json

Let's make a second fixture for unit testing - this one doesnt specifies only the
Doodle model's data to go into the fixture::

   python manage.py dumpdata --indent=4 doodle_app.Doodle > doodle_app/fixtures/test_data.json

In the next section we will look at how to write a simple unit test for our
model that uses our test fixture.
