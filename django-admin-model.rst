Model Administration
====================

Django provides a lot of rich functionality to you 'out of the box'. One really
nice feature is the `admin interface
<http://docs.djangoproject.com/en/dev/ref/contrib/admin/>`_. You can create a
default admin view view for each model and with a web GUI create, browse and so
on your models.

Lets add the admin view for our doodle model by editing
:file:`doodle_app/admin.py` (you need to create the file as it does not exist
by default). Now add this::

  from django.contrib import admin
  from models import Doodle

  class DoodleAdmin(admin.ModelAdmin):
      list_display = ('name', 'doodle_date') 
      list_filter = ('name', 'doodle_date')

   #Register each model with its associated admin class
   admin.site.register(Doodle, DoodleAdmin)

The process is to create an admin class for each of your models and then configure how you would like the models to be shown.

The optional list_filter and list_display determine which model properties can
be used for filtering and which should be used for displaying the model list
(see the screenshot further down).

.. note:: Our model inherits from admin.ModelAdmin.

Next register the django admin app with the controller by editing
:file:`django_project/urls.py` and make it look like this (by uncommenting the
appropriate lines)::
  
  from django.conf.urls import patterns, include, url 
  from django.contrib import admin
  admin.autodiscover()

  urlpatterns = patterns('',
      # Examples:
      # url(r'^$', 'django_project.views.home', name='home'),
      # url(r'^django_project/', include('django_project.foo.urls')),
      # Uncomment the admin/doc line below to enable admin documentation:
      # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

      # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
    )

You also need to enable the app by editing :file:`django_project/settings.py`
and adding the admin app to the installed apps list::
  
  INSTALLED_APPS = (
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.sites',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      # Uncomment the next line to enable the admin:
      'django.contrib.admin',  # <-- uncomment this line
      # Uncomment the next line to enable admin documentation:
      # 'django.contrib.admindocs',
      'django_extensions',
      'doodle_app',
  )

We need to tell django about our new admin model so we re-run syncdb:

:command:`python manage.py syncdb`

It should report something like this::
   
  $ python manage.py syncdb
  Creating tables ...
  Creating table django_admin_log   <-- new tables created
  Installing custom SQL ...
  Installing indexes ...
  Installed 0 object(s) from 0 fixture(s)


Now kill and restart the django server::

  ctrl-c
  python manage.py runserver

If you point your browser to : http://localhost:8000/admin/ you should now get a 
log in prompt and after that see the doodle model listed.

You can play around adding and deleting doodles using the admin interface.

.. image:: img/image004.png

.. image:: img/image005.png

.. image:: img/image006.png

In practice we probably won't use the admin interface very much since we will
spend most of the time on this course learning to build our own custom user
interfaces. However it is good to remember the admin functionality exists because
its really quick and easy to slap a simple web application together using only
models and the web admin interface.

