Testing Django Apps
===================

I'm diving into testing very early in this training manual and will emphaise it
all along. One of the great mistakes I made when learning django was not using
and understanding testing from the beginning. Having a good test suite if you
want to build a robust application.

Testing django applications uses the python unittest framework. There are
various add-ons out there in the community which can improve your testing
activities, but for now we will focus on getting the basics. We already showed
you how to create :doc:`django-fixtures`, which are an important cornerstone of
any test suite you build. Django creates a :file:`test.py` file for you
automatically when it creates your app, so let's implement a simple test for
our Doodle model there::

  from django.test import TestCase
  from models import Doodle

  class DoodleTest(TestCase):
      """Unit test for the Doodle model"""
      fixtures = ['test_data.json']

      def testCreation(self):
          """Test Doodle creation"""
          myCount = Doodle.objects.all().count()
          myDoodle = Doodle()
          myDoodle.name = 'Test Doodle'
          myDoodle.save()
          for myDoodle in Doodle.objects.all():
          print myDoodle.name
          myMessage = 'Expected one more doodle after creation'
          assert Doodle.objects.all().count() > myCount, myMessage


Note the following things:

* We import our Doodle model from :file:`models.py`
* Our DoodleTest class inherits from TestCase
* We can (optionally) define a list of fixtures that should be loaded before
  the test runs
* We use docstrings to describe the test
* The test failure or passing is determined by our assert statement
* Normally you shouldn't print stuff out unless the test fails (and then you
  should use assert's message parameter to do it.

Now we can run the test and see that everything passes::

  $ python manage.py test doodle_app
  Creating test database for alias 'default'...
  Tim Doodle
  foobar
  digettydoo
  Test Doodle
  .
  ----------------------------------------------------------------------
  Ran 1 test in 0.052s

  OK
  Destroying test database for alias 'default'...

Ok so now if we ever break our Doodle model, we will know about it!

Writing tests adds extra overhead in coding time and maintenance, but it will
save you tons of time as you can verify your whole code base every time you
change something.

We will continue to implement tests as we work through this tutorial, but lets
continue with our discussion of models by looking at the admin model in the
next section.
