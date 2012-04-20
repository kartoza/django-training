Models In Depth 
===============

In our quickstart run through in the previous section we created a simple model
and saw how you can manipulate the model using the django python console. We
also saw that you can create a user interface for the model quickly by using
the admin application that comes as a standard part of django.

The heart of Django is the :abbr:`ORM (Object Relational Mapping)` functionality it
provides. With Django, you program and think in python and the application
framework does all the nuts and bolts stuff behind the scenes or serialising
your saved models into the database and deserialising the models again when you
need to access them.

We saw a simple example of this, for example by doing::
  
  myDoodle.save()

A record was created in the database representing the model. And when we did::
  
  myDoodle2 = Doodle.objects.get(id=1)

The django framework took care of deserialising the model from the database and
making it available to us as a python object.

Models are by convention defined in :file:`<yourapp>/models.py`.

Defining a model is simply a matter of adding a new class to the above file.

The model creation consists of four steps:

+ Create a **new class** that inherits from //models.Model// in
  :file:`<yourapp>/models.py`. This class will be mapped to a table entity on the
  database backend.
+ Add the **property definitions** to your class. These will be mapped to
  fields in the table on the database backend.
+ Define the **metadata inner class**. This provides you a way to specify how 
  the models should be shown to the users and created in the database. For 
  example, you can use the metadata inner class to specify a non-default 
  backend table name.
+ Use the manage.py **syncdb** command to create the backend database model 
  and perform an integrity check of the model.

Lets look again at the model definition we created earlier, but with some extra
comments::

```
# Our base class
from django.db import models
# import GeoDjango stuff to support spatial data types
from django.contrib.gis.db import models
# Use python time goodies
import datetime

# A class defines our model if it inherits from models.model
class Doodle(models.Model):
  # Create a name field
  name = models.CharField(max_length=255)
  # And a geometry field for our doodle
  doodle = models.LineStringField(srid=4326,null=True, blank=True)
  # Lastly make an auto populated date field
  doodle_date = models.DateTimeField('DateAdded', 
                auto_now=True, auto_now_add=False)
  # Model manager that must be added to any model with a geometry
  objects = models.GeoManager()

  # Metadata inner class
  class Meta:
    # Name the table should be given on the database backend (optional)
    db_table = 'doodle'
    # Name to be used in the user interface (generated web pages) for this model
    verbose_name = ('Fantastic Doodle')
    # Plural name to be used in the user interface
    verbose_name_plural = ('Fantastic Doodles')
    # Column ordering to be used by default if a collection of model instances is
    # obtained.
    ordering = ('doodle_date','name',)

```

== Field Types ==

[Django field documentation http://docs.djangoproject.com/en/dev/ref/models/fields/]

There are a number of different field types you can use, including special
types that will build foriegn key constraints, multikey join tables, lookup
lists and so on. Here is a complete list of allowed types:

Standard field types:

```
AutoField
BooleanField
CharField
CommaSeparatedIntegerField
DateField
DateTimeField
DecimalField
EmailField
FileField
FilePathField
FloatField
ImageField
IntegerField
IPAddressField
NullBooleanField
PositiveIntegerField
PositiveSmallIntegerField
SlugField
SmallIntegerField
TextField
TimeField
URLField
XMLField
```

Relationship fields:

```
ForeignKey
ManyToManyField
OneToOneField
```

Spatial field types:

```
PointField
LineStringField
PolygonField
MultiPointField
MultiLineStringField
MultiPolygonField
GeometryCollectionField
```

== Verbose Names ==

You can use verbose_name to give the model field a more friendly name that will
be shown on forms etc. **Note:** for foreign key and other relationship fields,
you must place the verbose name **after** the relation name. e.g.

```
status = models.ForeignKey(Status,verbose_name="Order Status")
```

== Choices ==

If you want to restrict the values that a user can choose from in order to
populate the field. You can do this using a list e.g.:

```
myChoices = (("a" , "Pothole"), ("b" , "Road Sign"), ("c" , "Vagrants"))
```

Then when you create your field you would do:

```
name = models.CharField(max_length=255,choices=myChoices)
```

If you open the doodle model in the admin web interface, you should see that
the text field for name is now replaced with a combo with the items listed in
myChoices in it.

Personally I think using the choices option is usually better implemented using
a separate model and then using a relationship field. If you are really sure
the choices list will never change, you could use it. Let me show you how we
would rather implement the choice using a second model and a relationship
field.

== Relationship fields ==

First delete the myChoices... line we created above. Next add a new class to
models.py (put it before the doodle class) that looks like this:


```
class DoodleType(models.Model):
  name = models.CharField(max_length=255)
  objects = models.Manager()

  def __unicode__(self):
    return self.name


  class Meta:
    db_table = 'doodletype'
    verbose_name = ('Doodle Type')
    verbose_name_plural = ('Doodle Types')
    ordering = ('name',)

```

Next, change the doodle.name field from a charfield to one that looks like this:

```
  name = models.CharField(max_length=255)
```

And add doodle.type like this:

```
  type = models.ForeignKey(DoodleType)
```

''Note:'' if you want to, you can specify a default value across the ForeignKey relate by doing e.g.

```
doodle_type = models.ForeignKey(DoodleType, default=DoodleType.objects.get(id=1))
```

(which uses the first instance of doodle type as the default value).

To register the changes in our models, you need to run syncdb again. However we
have changed an existing model's field type (Doodle.name) which means that
model's table definition also needs to be synced to the database. Before we can
do that we need to drop its table. We will discuss later how to deal with data
that may be in a table if you need to replace it with one that contains
existing functionality:

```
echo "drop table doodle;" > psql django_project
python manage.py syncdb
```

or

```
python manage.py sqlreset doodle | psql django_project
```

Finally to test, we need to add a new entry to doodle/admin.py...:

```
from django.contrib.gis import admin
from models import *

class DoodleTypeAdmin(admin.ModelAdmin):
  list_display = ('name',) 

class DoodleAdmin(admin.GeoModelAdmin):
  field = (None, {'fields': ('name')})
  field = (None, {'fields': ('doodle')})
  field = (None, {'fields': ('doodle_date')})
  list_display = ('name', 'doodle_date', 'doodle') 
  list_filter = ('name', 'doodle_date')

#Register each model with its associated admin class
admin.site.register(DoodleType, DoodleTypeAdmin)
admin.site.register(Doodle, DoodleAdmin)
```

Registering the DoodleType model in the admin interface is much simpler since
it does not contain any geometry fields. Django only needs the line 

```
admin.site.register(DoodleType, DoodleTypeAdmin)
```

added to admin.py and it will do all the rest. If you go back to your doodle
admin interface now it should look something like this:

[img/doodleadmin.png]

You will notice there is now a little + icon next to the Name field. If you
click on it, the admin interface will pop up a form where you can manage the
list of names in the DoodleType model.

== One last thing ==

If you were alert, you might have wondered what is to prevent the same
DoodleType name being added twice. In fact django automatically added a unique
constraint to that field:

```
django_project=# \d doodletype
Table "public.doodletype"
 Column |          Type          |                        Modifiers                        
--------+------------------------+---------------------------------------------------------
 id     | integer                | not null default nextval('doodletype_id_seq'::regclass)
 name   | character varying(255) | not null
Indexes:
"doodletype_pkey" PRIMARY KEY, btree (id)
"doodletype_name_key" UNIQUE, btree (name)

```

So you will see in the next snippet what would happen if you try to insert a
duplicate record:

```
django_project=# select * from doodletype;
 id | name 
----+------
  1 | Test
(1 row)

   django_project=# insert into doodletype (name) values ('Test');
   ERROR:  duplicate key value violates unique constraint "doodletype_name_key"

```

Once again django just takes care of stuff for you in the background and you
don't need to worry about too many small details...

