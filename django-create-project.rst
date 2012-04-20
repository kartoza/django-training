Your First Project
==================

A project can contain one or more applications. We will use 
the postgis backend here though various other backends are 
supported and more are on the way. Lets create our first project::

   cd /home/web/django-training
   source python/bin/activate
   django-admin.py startproject django_project
   cd django_project/

.. note::  A project name can only use numbers, letters and underscores.


Configure your project
----------------------

At this point you should fill in the database connection settings (in settings.py)::

  'ENGINE': 'django.db.backends.sqlite3', 
  'NAME': 'django.db'

Also set the time zone::
   
   TIME_ZONE = 'Africa/Johannesburg'


Then save and close the settings.py file and do::
   
   python manage.py runserver

You should now be able to visit your project here at http://localhost:8000

.. note:: Note you can use any port you like.

Your browser should show a message something like this::

   It worked!
   Congratulations on your first Django-powered page.
   
   Of course, you haven't actually done any work yet. Here's what to do next:

   * If you plan to use a database, edit the DATABASE_* settings in django_project/settings.py.
   * Start your first app by running python django_project/manage.py startapp [appname].

   You're seeing this message because you have DEBUG = True in your Django
   settings file and you haven't configured any URLs. Get to work!


Lets take another look at our directory structure now::

   django-training
   |-- django_project
   |-- | django_project
   |     |-- __init__.py
   |     |-- settings.py
   |     `-- urls.py
   |-- | manage.py
   `-- python
       |-- bin
       |-- include
       `-- lib


.. note:: Before version 1.4 of django the project was a flat directory. As 
   of 1.4 it contains an internal directory by the same name for settings etc.

As you can see from the above diagram, django has created a basic project 
framework for us under the directory entitled 'django_project'.

Make an application
-------------------

As we said above, a project contains one or more applications. All apps in the
project use a global settings and urls file (which we will look at in more
detail just now). First we will create a simple application.

First kill the server by pressing :kbd:`ctrl-c` and then do::

   cd /home/web/django-training/django_project/
   python manage.py startapp doodle_app

Doing that creates a new directory under our project called doodle_app::

   django
   |-- django_project
   |   |-- doodle_app
   |   |   |-- __init__.py
   |   |   |-- models.py
   |   |   |-- tests.py
   |   |   `-- views.py
   |-- |-- django_project
   |     |-- __init__.py
   |     |-- settings.py
   |     `-- urls.py
   |   |-- __init__.py
   |   |-- manage.py
   `-- python
       |-- bin
       |   |-- activate
       |-- include
       `-- lib

You can see the creation of our doodle app introduced some new 
files into our directory tree:

* **models.py** - where we define our models
* **views.py** - where we define our views

Where is the controller? **urls.py** in the top level project dir is our default
controller - it decodes urls and sends requests on to the correct view class.

Before we can use our application, we need to register it with settings.py and 
run 'syncdb' which synchronises our application settings to the django database.

To register the new application, edit :file:`django_project\django_project\settings.py` and add it to the bottom of the list of INSTALLED_APPS::
  
  INSTALLED_APPS = ( 
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.sites',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      # Uncomment the next line to enable the admin:
      # 'django.contrib.admin',
      # Uncomment the next line to enable admin documentation:
      # 'django.contrib.admindocs',
      'doodle_app',  # <-- new application added
    )

:command:`python manage.py syncdb`

Which will produce something like this::

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
   
   You just installed Django's auth system, which means you don't have any superusers defined.
   Would you like to create one now? (yes/no): yes
   Username (leave blank to use 'timlinux'): 
   E-mail address: tim@linfiniti.com
   Password: 
   Password (again): 
   Superuser created successfully.
   Installing custom SQL ...
   Installing indexes ...
   Installed 0 object(s) from 0 fixture(s)


Now we have an application - we can visit it like this:

Make sure the test server is running first::
   
   cd /home/web/django-training/django_project/
   source ../python/bin/activate
   python manage.py runserver

.. note:: The source and cd commands above are only needed if you have started 
   a new shell session and or changed to a different directory in the meantime.


Now point your browser at the app : http://localhost:8000/doodle_app/

You should see a basic placeholder message. In the lessons that
follow we will customise the application in various ways and learn about django
architecture in the process.
