Django Installation
===================

Creating the top level working dir
----------------------------------

Django is available in apt, but this will be one of the few times I break my
rule about preferring apt installed packages over hand installed.

Instead we will use something called a 'python virtual environment' * which is 
considered to be the best practice for deploying a django project.

We will begin by creating a top level working directory e.g.::

   mkdir -p /home/web/django-training
   cd /home/web/django-training


Understanding the directory structure
-------------------------------------

In our next step we will set up our virtual environment. We are aiming to end up 
with something like this::

   django-training
   |-- project1
   |   |-- app1
   |   `-- app2
   |-- project2
   |   |-- app1
   |   `-- app2
   `-- python   <-- virtual environment for python

Django divides your work into projects and applications. A ''project'' provides 
shared templates, media (images, logos etc) to its applications and a shared
user database and so on.

An ''application'' provides some specific functionality. You can also install 
third party applications under your project directory to provide things like 
login frameworks etc.

We will get on to how projects and applications are created in a minute, but first 
lets get our python virtual environment set up...

Creating the virtual environment
--------------------------------

To create your virtual environment, make sure you are in the 
django directory we created above first and then do::

   sudo apt-get install python-setuptools build-essential python-dev libpq-dev
   sudo easy_install virtualenv
   virtualenv --no-site-packages python
   source python/bin/activate
   easy_install pip
          

What have we just done? We have set up a virtual environment (think of it 
as a simplified version of a virtual machine). In the virtual environment,
we have a repeatable, easily backed up and independent set of python 
libraries used to drive the django web site we are going to create.

+ **Repeatable** : you can easily deploy your application to another machine
+ **Easily backed up** : you just backup the whole of your django dir and
  then you have a backup of not only your django project, but also 
  the python libs needed to run it.
+ **Independent** : If the system libraries change, it should not affect 
     your web site.

Install Django into the Virtual Environment
-------------------------------------------


Now we want to install django and a few other pre-requisites into the 
virtual environment::

   pip install django
   pip install django-registration
   pip install django-debug-toolbar
   pip install django-extensions
   pip install psycopg2
   pip install ipython


You need to be connected to the internet for the above commands to work. 
The above commands install django, psycopg2 (which lets python connect to 
postgresql databases) and a few other useful django applications which 
we will use later in this tutuorial.

In case you are wondering, pip is a package management tool for python.

Following the above steps, your directory structure should now look like this::

   django-training
   `-- python
       |-- bin
       |   |-- activate
       |   |-- activate_this.py
       |   |-- django-admin.py
       |   |-- easy_install
       |   |-- easy_install-2.6
       |   |-- pip
       |   `-- python
       |-- include
       |   `-- python2.7 -> /usr/include/python2.7
       `-- lib
           `-- python2.7


Activate the virtual env
------------------------

Whenever you start a shell session, you need to source the activate script to
enabled the python virtual environment::

   source python/bin/activate


This sets up the system search path for python to look into your virtual env. 
in preference over using the system libs under /usr/lib/python.

Setup Postgresql
----------------

You don't need to use postgresql with django - it supports a variety of 
other databases. But its a good choice for a backend especially in light 
of the support for spatial datasets via PostGIS, so lets install and use it::
   
   sudo apt-get install postgresql-8.4-postgis


Initial project setup
---------------------

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
