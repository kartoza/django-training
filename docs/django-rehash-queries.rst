Object Queries
==============

It is important to get queries efficiently from the database. The ORM provides
a rich set of options to achieve this.

Through the Model class's objects interface it is possible to access various
methods.

Get A Single Model
------------------

To select a specific entry in the database the get() function can be called.
It is your responsibility to make sure that only one object is ever returned
here. If there are no or multiple entries that match the request, we will
receive an error, which we will need to handle.

Get A Query Set
---------------

A queryset is returned when the below functions are called. These are all
chanable and are only evaluated at the last possible moment.

All
---

In order to get all entries in a table the all() function is used.


Filter
------

The filter() function is used to get a subset of all entries. The filter
function includes everything that matches the arguments provided.

Exclude
-------

The exclude() function removes matching objects from the queryset.

Ordering
--------

Once a queryset is returned, the results will be listed in the default order,
unless a different order is specified by an order_by() call


Lookup Variables
----------------

The get(), filter(), and exclude() functions each take keywords. These are
based on field names in the model object. To specify various types of tests
on these names a double _ (``__``) notation is used.

The following are valid forms of this:

 - field_name='some text': Only an exact match is returned here.
 - field_name__iexact='SoME TeXt': Match a case insnsitive version of the text.
 - field_name__contains="ome": Select if any part of the text matches this string.
 - field_name__contains="ome": Select if any part of the text matches this string, case insensitive.
 - field_name__startswith="some": Select if this is the first bit of the text.
 - field_name__istartswith="some": Case insensitive version
 - field_name__endswith="text": Selects if this is the lat bit of the text.
 - field_name__iendswith="text": Case insensitive version
 - field_name__gt="7": Select objects greater than the value
 - field_name__gte="7": Select objects greater than or equal to the value
 - field_name__lt="5": Select objects less than the value
 - field_name__lte="5": Select objects less than or equal to the value


Using foreign fields to access fields in related models

 - field_name__relate_field__*: Do a check on a related table's field.


Chaining
--------

The arguments inside a filter would typically constitute an AND relationship.
If we would chain a filter, this would amount to an OR  relationship.

Complex Lookups
---------------

If you need to do something more involved a Q object can be used. This object
can be imported as follows::

   from django.db.models import Q

These can also be put together in one argument using the & or | or for
anding and oring respectively.

Dropping To SQL
---------------

In some rare cases extreme efficiency is required or a lookup is too complex
to chain. Then you may want to hand code the SQL that will be getting the
model data. This can be done using the raw() function.