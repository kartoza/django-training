Testing
=======

Testing gives you the ability to find bugs, before the code reaches the user.
Testing is hence very important. Leading to resolutions before problems are
encountered.


Consider our test scaffolding in ``TestThis``. This provides the basic
scaffolding for our tests. Each method starting with ``test_`` is
a test and is evaluated when testing.

Try a dummy test run using::

    python manage.py test


We will find that this test passes. So far it is not testing anything in our
app though.

Exercise
--------

Update the unicode method of our InterestZone to include the name and
acquisition_date. In our test create a model and assert that this is the case.

Factory Boy
-----------

In our test cases we often need many objects in the database. Obviously this
can become quite tedious. Especially if anything changes in our model. We
would end up spending more time updating tests than actually writing production
code.

That is where factoryboy comes in quite handy. This application uses
predefined rules to create models which are valid::

	import factory
	from demo_app.models import ZoneType

	class ZoneFactory(factory.django.DjangoModelFactory):
		class Meta:
			model = ZoneType

		name = factory.Sequence(lambda n: "zone_%d" % n)

This factory will create a class with a zone named = zone_n where n is n'th
time this factory is creating a model.

Let's try it::

	zone_types = ZoneType(amount=100)


Exercise
--------

Add a factory for InterestZone and update the test above.
