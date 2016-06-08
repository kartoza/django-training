Models In Depth
===============

The heart of Django is the :abbr:`ORM (Object Relational Mapping)` functionality it
provides. With Django, you program and think in python and the application
framework does all the nuts and bolts stuff behind the scenes or serialising
your saved models into the database and deserialising the models again when you
need to access them.


Connecting The Datable
----------------------

The models we create need to persist. This is typically done in a database.
We will be using postgres (with postgis enabled). We are defining this as the
default database::

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': {{ DATABASE_NAME }},
            'USER': {{ DATABASE_USERNAME }},
            'PASSWORD': {{ DATABASE_PASSWORD }},
            'HOST': 'localhost',
            'PORT': 5432,
            'TEST_NAME': 'unittests',
        }
    }

Now our model objects, once saved will land up in this database. Let's have a
look at this in the django shell::

   >>> from demo_app.models import ZoneType
   >>> zone_type.objects.all()  # You should get nothing back
   >>> zone_type = ZoneType()
   >>> zone_type.name = 'zone 1'
   >>> zone_type.save()
   >>> zone_type.objects.all()  # Zone1 added
   >>> zoen_type.objects.get(id=1) # Get only the first zone


The django framework took care of deserialising the model from the database and
making it available to us as a python object. Models are by convention defined
in :file:`<yourapp>/models.py`. Defining a model is simply a matter of adding
a new class to the above file.

The model creation consists of four steps:

+ Create a **new class** that inherits from //models.Model// in
  :file:`<yourapp>/models.py`. This class will be mapped to a table entity
  on the database backend.
+ Add the **property definitions** to your class. These will be mapped to
  fields in the table on the database backend.
+ Define the **metadata inner class**. This provides you a way to specify how 
  the models should be shown to the users and created in the database. For 
  example, you can use the metadata inner class to specify a non-default 
  backend table name.
+ Use the manage.py **makemigrations** and **migrate** commands to create
  the backend database model.

Lets look at the model definition we created earlier, but with some extra
comments::
   
   class InterestZone(models.Model):
       """A class defines our model if it inherits from models.model"""
       name = models.CharField(max_length=255)
       """The name of our interest zone"""
       zone_type = models.ForeignKey(ZoneType)
       """The zone type this zone is linked to."""
       doodle_date = models.DateTimeField('DateAdded', 
           auto_now=True, auto_now_add=False)
       """An auto populated date field"""
       geometry = models.PolygonField(
           srid=4326, null=True, blank=True, help_text='Area')
       """The geometry of the zone"""
       objects = models.GeoManager()
       """Optional name for the model manager instance for this model."""

       class Meta:
           """Meta (inner) class for our Doodle model"""
            verbose_name = ('Interest Zone')
            """Name to be used in the user interface (generated web pages) for
            this model (defaults to model name)."""
            verbose_name_plural = ('Interest Zones')
            """Plural name to be used in the user interface (a default
            pluralisation will be given if none specified)."""
            ordering = ('acquisition_date','name',)
            """Column ordering to be used by default if a collection of model
            instances is obtained."""

Field Types
-----------

The different types of field that you can use in django models are described in
the `Django documentation <http://docs.djangoproject.com/en/dev/ref/models/fields/>`_.
There are a number of different field types you can use, including special
types that will build foriegn key constraints, multikey join tables, lookup
lists and so on. Here is a complete list of allowed types:

Standard field types:

* AutoField
* BooleanField
* CharField
* CommaSeparatedIntegerField
* DateField
* DateTimeField
* DecimalField
* EmailField
* FileField
* FilePathField
* FloatField
* ImageField
* IntegerField
* IPAddressField
* NullBooleanField
* PositiveIntegerField
* PositiveSmallIntegerField
* SlugField
* SmallIntegerField
* TextField
* TimeField
* URLField
* XMLField

Relationship fields:

* ForeignKey
* ManyToManyField
* OneToOneField

Spatial field types:

* PointField
* LineStringField
* PolygonField
* MultiPointField
* MultiLineStringField
* MultiPolygonField
* GeometryCollectionField

Verbose Names
-------------

You can use :keyword:`verbose_name` to give the model field a more friendly name
 hat will be shown on forms etc. 

.. note:: For foreign key and other relationship fields, you must place the
  verbose name **after** the relation name. e.g::
   
   status = models.ForeignKey(Status,verbose_name="Order Status")


Choices
-------

If you want to restrict the values that a user can choose from in order to
populate the field. You can do this using a list e.g.::
   
   myChoices = (("a" , "Pothole"), ("b" , "Road Sign"), ("c" , "Vagrants"))

Then when you create your field you would do::
   
   name = models.CharField(max_length=255,choices=myChoices)

If you open the doodle model in the admin web interface, you should see that
the text field for name is now replaced with a combo with the items listed in
myChoices in it.

Personally I think using the choices option is usually better implemented using
a separate model and then using a relationship field. If you are really sure
the choices list will never change, you could use it. Let me show you how we
would rather implement the choice using a second model and a relationship
field.

Relationship fields
-------------------

Relationship fields are used to express foreign key joins - you can have
one-to-many, many-to-many etc. type relationships. The underlying 'plumbing' of
these relationships is built for you in the backend database by Django.

The foreignkey that is defined in our model links it to one ZoneType.
using a OneToOne would make that connection go both ways.

ManyToMany fields allow for any number of connections to be made between
models, under the hood this is done using a table with matching ids.

Exercise
--------

We would like our models to have multiple zones that they are assigned to.
After you have made your changes run::

    python manage.py makemigrations
    python manage.py migrate


Let's have a look at the newly created migration.

Migrations
----------

Migrations are used to transform the state of the database. This can have
one of two forms as we saw above the schema was changed when we went
from a foreignkey to ManyToMany. But what if we find the data is in a bad state
and we need to fix some underlying issue in the data. This can be done using
a data migration.

Exercise
--------

Update this migration code, to ensure all ZoneTypes are in camelcase, with no
spaces. Here is a skeleton::

    from django.db import migrations

    def forwards(apps, schema_editor):
         ZoneType = apps.get_model('demo_app', 'ZoneType')
         # Your code here


    class Migration(migrations.Migration):

        dependencies = [
            # Update this to the latest app
            ('demo_app' ),
        ]

        operations = [
            migrations.RunPython(forwards,
            reverse_code=migrations.RunPython.noop,
            hints={'target_db': 'default'}),
        ]
