Your First Project
==================

A project can contain one or more applications. We will use 
the postgis backend here though various other backends are 
supported and more are on the way. Lets create our first project::

   cd /home/web/django-training
   source python/bin/activate
   django-admin.py startproject django_project
   cd django_project/
   createdb django_project
   createlang plpgsql django_project
   psql django_project < /usr/share/postgresql-8.3-postgis/lwpostgis.sql
   psql django_project < /usr/share/postgresql-8.3-postgis/spatial_ref_sys.sql 

.. note:: If you are using a different version of postgresql those last two
   lines should be adjusted accordingly.


Setup your Database connection
------------------------------

At this point you should fill in the database connection settings (in settings.py)::

   # Note delete django.db.backends.
   DATABASE_ENGINE = 'postgresql_psycopg2'
   DATABASE_NAME = 'django_project'
   DATABASE_USER = 'foouser'
   DATABASE_PASSWORD = 'foopassword'
   DATABASE_HOST = 'localhost'
   DATABASE_PORT = '5432'

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
   |   |-- __init__.py
   |   |-- manage.py
   |   |-- settings.py
   |   `-- urls.py
   `-- python
       |-- bin
       |-- include
       `-- lib

As you can see from the above diagram, django has created a basic project 
framework for us under the directory entitled 'django_project'.

Make an application
-------------------

As we said above, a project contains one or more applications. All apps in the
project use a global settings and urls file (which we will look at in more
detail just now). First we will create a simple application.

First kill the server by pressing :kbd:`ctrl-c` and then do::

   cd /home/web/django/django_project/
   python manage.py startapp doodle-app

Doing that creates a new directory under our project called doodle-app::

   django
   |-- django_project
   |   |-- doodle-app
   |   |   |-- __init__.py
   |   |   |-- models.py
   |   |   |-- tests.py
   |   |   `-- views.py
   |   |-- __init__.py
   |   |-- __init__.pyc
   |   |-- manage.py
   |   |-- settings.py
   |   |-- settings.pyc
   |   `-- urls.py
   `-- python
       |-- bin
       |   |-- activate
       |-- include
       `-- lib

You can see the creation of our doodle app introduced some new 
files into our directory tree:

* **models.py** - where we define our models
* **views.py** - where we define our views

Where is the controller? **urls.py** in the top level project dir is our
controller - it decodes urls and sends requests on to the correct view class.

Now we have an application - we can visit it like this:

Make sure the test server is running first::
   
   cd /home/web/django-training/django_project/
   source ../python/bin/activate
   python manage.py runserver

.. note:: The source and cd commands above are only needed if you have started 
   a new shell session and or changed to a different directory in the meantime.


Now point your browser at the app : http://localhost:8000/doodle-app/

You should see a basic placeholder message.

Congratulations! You just made your first django app. In the lessons that
follow we will customise the application in various ways and learn about django
architecture in the process.
