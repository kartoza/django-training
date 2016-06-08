Model Administration
====================

Django provides a lot of rich functionality to you 'out of the box'. One really
nice feature is the `admin interface
<http://docs.djangoproject.com/en/dev/ref/contrib/admin/>`_. You can create a
default admin view view for each model and with a web GUI create, browse and so
on your models.

:file:`demo_app/admin.py` (You would need to create the file as it
would not exist by default). ::

    from django.contrib import admin
    from django.contrib.gis import admin
    from demo_app.models import ZoneType, InterestZone


    class InterestZoneAdmin(admin.OSMGeoAdmin):
        list_display = ('name', 'acquisition_date')
        list_filter = ('name', 'acquisition_date')


    # Register each model with its associated admin class
    admin.site.register(InterestZone, InterestZoneAdmin)


The process is to create an admin class for each of your models and then
configure how you would like the models to be shown.

The optional list_filter and list_display determine which model properties can
be used for filtering and which should be used for displaying the model list.

Make sure that this is added in our core urls::

    url(r'^demo-admin/', include(admin.site.urls)),

This is already included in our demo app, please go verify this
at :file:`core/settings/base.py` making sure the admin app to the
installed apps list.

now create a superuser by running::

    python manage.py createsuperuser


If you point your browser to : http://0.0.0.0:888/demo-admin/ you
should now get a log in prompt and after that see the models listed.

Exercise
--------

As you can see the ZoneType is not available in the admin. Update the admin
to include the zone type models.