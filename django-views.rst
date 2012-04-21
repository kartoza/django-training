Views 
=====

Ok by now you should understand the basic concept of a model - you define it
using a python :keyword:`class`, synchronise the database to your model
definitions, and then you can add the model to the admin user interface if you
want to get a quick & dirty UI for your models.

Invariably however, you will want to create your own views and forms. In other
words, you will want your site to have its own unique look and feel and user
interactions, rather than the canned environment of the admin interface.

To do that will start by delving into views a little.

Hello World
-----------

I bet you have been waiting for this moment :-) While a model represents an
object or entity, a view represents a particular view of an object or group
of objects. We can also have a view that does not reflect the state of any
particular object, but rather just some hard coded information - which is what
we will look at first - we are going to make a view that returns ``Hello World``
as a string.

Hello World Test
----------------

Since we are promoting test driven development here, let's write a test first
and then implement the view. We can write it in :file:`doodle_app/tests.py`::
   
   from django.test.client import RequestFactory
   from views import helloWorld
   
   class TestViews(TestCase):
       """    Tests that doodle_app views work."""
   
       def setUp(self):
           """very test needs access to the request factory.
              So we create it here"""
           self.factory = RequestFactory()
   
       def testHelloWorldView(self):
           """Test hello world view works."""
           myRequest = self.factory.get('/helloWorld')
           myResponse = helloWorld(myRequest)
           self.assertEqual(myResponse.status_code, 200)
           myExpectedString = '<h1>Hello World</h1>'
           myMessage = ('Unexpected response from helloWorld'
                        ' - got %s, expected %s' %
                        (myResponse.content, myExpectedString))
           self.assertEqual(myResponse.content, myExpectedString, myMessage)

When you try to run this test, you expect a failure (since we haven't actually
written our view yet), but we have defined the preconditions under which the
test should pass, so we know that as soon as it does pass, our work is done!

So run the test and you should get output which ends something like this::
   
   File "/home/web/django-training/django_project/doodle_app/tests.py", line 5, in <module>
   from views import helloWorld
   ImportError: cannot import name helloWorld

Good our test fails! Lets implement the view now...

Hello World Implementation
--------------------------

Open up your doodle/views.py file. It should contain something like this::
   
   # Create your views here.

Looks like someone was here before us then eh? The views stub was created when
we created our application. Views in django are simply function definitions so
we can create one like this::
   
   from django.http import HttpResponse
   
   
   def helloWorld(theRequest):
       """A simple hello world view"""
       return HttpResponse('<h1>Hello World</h1>')


Thats about the simplest view you can make. The HttpResponse class knows how to
return any string you give it as a web page back to the clients browser.

You will notice that the helloWorld view takes a single parameter 'theRequest'
which is an object containing all of the request context information from the
client. For example it has any form post variables, the user agent (which
browser is being used) etc. Since this is a really simple view the request
parameter is actually ignored, but we will see later how to make good use of
it. For now you should note that every view is passed a request in its
signature.

Test the view
-------------

Ok now we can run our tests again (:command:`python manage.py test doodle_app`)
which should produce output like this::
   
   Creating test database for alias 'default'...
   Doodel 1
   Doodle 2
   Doodle 3
   Test Doodle
   .Hello World OK
   .
   ----------------------------------------------------------------------
   Ran 2 tests in 0.010s
   
   OK
   Destroying test database for alias 'default'...

The controller
--------------

Remember we are implementing the :abbr:`Model View Controller (MVC)` design
pattern here. We have a model (:keyword:`Doodle`), we have a view
(:keyword:`helloWorld`). Now lets implement the controller. The idea is to
make our view available at the url http://localhost:8000/helloWorld/.

Controller Test
---------------

Of course we should first write a test, and then implement our controller, that
way we will know when we have written exactly enough code for our new feature.

Here is my updated :file:`doodle_app/tests/py` file in its entirety::
   
   from django.test import TestCase
   from models import Doodle
   from models import DoodleType
   from django.test.client import RequestFactory
   from views import helloWorld
   from django.test.client import Client
   
   class DoodleTest(TestCase):
       """Unit test for the Doodle model"""
       fixtures = ['test_data.json']
   
       def testCreation(self):
           """Test Doodle creation"""
           myCount = Doodle.objects.all().count()
           myDoodle = Doodle()
           myDoodle.name = 'Test Doodle'
           myDoodleType = DoodleType.objects.get(id=1)
           myDoodle.doodle_type = myDoodleType
           myDoodle.save()
           for myDoodle in Doodle.objects.all():
               print myDoodle.name
           myMessage = 'Expected one more doodle after creation'
           assert Doodle.objects.all().count() > myCount, myMessage
   
   
   class TestViews(TestCase):
       """    Tests that doodle_app views work."""
   
       def setUp(self):
           """very test needs access to the request factory.
              So we create it here"""
           self.factory = RequestFactory()
   
       def testHelloWorldView(self):
           """Test hello world view works."""
           myRequest = self.factory.get('/helloWorld')
           myResponse = helloWorld(myRequest)
           self.assertEqual(myResponse.status_code, 200)
           myExpectedString = '<h1>Hello World</h1>'
           myMessage = ('Unexpected response from helloWorld'
                        ' - got %s, expected %s' %
                        (myResponse.content, myExpectedString))
           self.assertEqual(myResponse.content, myExpectedString, myMessage)
           print 'Hello World View OK'
   
       def testHelloWorldUrl(self):
           """Test that the helloWorld url works using the django test web client.
           """
           myClient = Client()
           myResponse = myClient.get('/helloWorld/')
           self.assertEqual(myResponse.status_code, 200)
           myExpectedString = '<h1>Hello World</h1>'
           myMessage = ('Unexpected response from helloWorld'
                        ' - got %s, expected %s' %
                        (myResponse.content, myExpectedString))
           self.assertEqual(myResponse.content, myExpectedString, myMessage)
           print 'Hello World View OK'

You can see we are starting to repeat some code - a good indication that 
some refactoring is needed! Let's run our test now and see what happens.::'
   
   ======================================================================
   ERROR: testHelloWorldUrl (doodle_app.tests.TestViews)
   Test that the helloWorld url works using the django test web client.
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "/home/web/django-training/django_project/doodle_app/tests.py", line 50, in testHelloWorldUrl
       myResponse = myClient.get('/helloWorld/')
     File "/home/web/django-training/python/local/lib/python2.7/site-packages/django/test/client.py", line 439, in get
       response = super(Client, self).get(path, data=data, **extra)
     File "/home/web/django-training/python/local/lib/python2.7/site-packages/django/test/client.py", line 244, in get
       return self.request(**r)
     File "/home/web/django-training/python/local/lib/python2.7/site-packages/django/core/handlers/base.py", line 150, in get_response
       response = callback(request, **param_dict)
     File "/home/web/django-training/python/local/lib/python2.7/site-packages/django/utils/decorators.py", line 91, in _wrapped_view
       response = view_func(request, *args, **kwargs)
     File "/home/web/django-training/python/local/lib/python2.7/site-packages/django/views/defaults.py", line 20, in page_not_found
       t = loader.get_template(template_name) # You need to create a 404.html template.
     File "/home/web/django-training/python/local/lib/python2.7/site-packages/django/template/loader.py", line 145, in get_template
       template, origin = find_template(template_name)
     File "/home/web/django-training/python/local/lib/python2.7/site-packages/django/template/loader.py", line 138, in find_template
       raise TemplateDoesNotExist(name)
   TemplateDoesNotExist: 404.html
   
   ----------------------------------------------------------------------
   Ran 3 tests in 0.050s
   
   FAILED (errors=1)
   Destroying test database for alias 'default'...


So how does the client (i.e. you operating your web browser) get to see the 
view? You need to add a rule to our controller. This is done in the urls.py
file::




```
from django.conf.urls.defaults import *
# So we can find our hello world views
from doodle.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_project/', include('django_project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # For our hello world view
    (r'^helloWorld/', helloWorld),
)

```

Earlier we used our urls.py file to configure support for the admin interface.
Now I have added the following two lines to support our hello world view:

```
# So we can find our hello world views
from doodle.views import *

```

...and...

```
    # For our hellow world view
    (r'^helloWorld/', helloWorld),
```

The first new line just lets the controller (urls.py) know where to find our
views (doodle.views). The second addition adds a rule to urlpatterns. The rule
is a regular expression saying 'if the url starts with helloWorld, render the
helloWorld view'. Simple eh?

Try pointing your browser to your django instance now and see if you get a
hello world message back:

```
http://localhost:8000/helloWorld/
```

should show:

```
Hello World
```

== A view that takes a parameter ==

Django uses restful style urls to pass instructions and parameters to the
controller. Say, for example, you want to get a personalised greeting when you
connect to a view e.g.:

```
Hello Tim!
```

First we would defined a new view that takes a parameter (in doodle/views.py):

```
def helloPerson(theRequest,thePerson):
  return HttpResponse("<h1>Hello " + str(thePerson) + "!</h1>")
```

So that will take an extra parameter and print it in the response. Of course we
still need to add a rule to our controller...(in urls.py):

```
# For our hello person view
(r'^helloPerson/(?P<thePerson>[a-zA-Z]+)/$', helloPerson),
```

Ok that looks a bit greek like? Lets break it down:

```
r                        <-- what follows in quotes is a regular expression
^                        <-- carat means 'start of the line' 
                             note the http://localhost:8000/
                             part of the url is ignored in url matching
helloPerson/             <-- the literal string is matched here
(?P<thePerson>[a-zA-Z]+) <-- match any number of upper case or lower case
                             letters to the view parameter 'thePerson'
/$                       <-- end of the line
```

So in plain english it means 'if the url starts with /helloPerson/ followed by
any sequence of upper or lower case characters, assign that character sequence
to a variable called "thePerson" and pass it on to the helloPerson view.

Make sense? It will make more sense as you get a bit more experience with
django. Lets test out our new view:

```
http://localhost:8000/helloPerson/Tim/
```

...should show this...

```
Hello Tim!
```

== A view that works with models ==

Ok thats very nifty but in the real world, nine times out of ten you want your view to interact with model data. First add a few more entries to your DoodleType table using the admin web interface. Now lets make a view that shows a list of DoodleTypes (in doodle/views.py):

```
from doodle.models import *
def listDoodleTypes(theRequest):
  myObjects = DoodleType.objects.all()
  # Optional - sort descending:
  #myObjects = DoodleType.objects.all().order_by("-name")
  myResult = "<h1>doodle types</h1>"
  for myObject in myObjects:
    myResult = myResult +str(myObject.id) + " : " + str(myObject.name) + "<br />"
  return HttpResponse(myResult)
```

The view simply gets all the DoodleType objects (remember django's ORM
seamlessly pulls these from the database backend for you) and the loops through
them building up a string. The string is then returned to the browser using the
HttpResponse call.

Before we can see the view, you need to add a new rule to the controller.
Sensing a ryhthmn here? Good it is the same process over and over - create
models, make views on to your models, define controller rules so that you can
get to your views. So to make our new controller rule, we add a line in
urls.py:

```
# For our list doodle types view
(r'^listDoodleTypes/', listDoodleTypes),
```

Now point your browser at the new view:

```
http://localhost:8000/listDoodleTypes/
```

and you should see something like this:

```
Doodle Types
Test Type 1
Test Type 2
```

== A view of a single object ==

Ok so now we have a view that is driven by the data in our model. What if we
want to see just a specific model instance? We can use the get() call to do
that (in doodle/views.py):

```
def showDoodleType(theRequest, theId):
  myObject = DoodleType.objects.get(id=theId)
  myResult = "<h1>Doodle Type Details</h1>"
  myResult = myResult + "Id: " + str(myObject.id) + "<br />"
  myResult = myResult + "Name: " + str(myObject.name) + "<br />"
  return HttpResponse(myResult)
```

And a rule to our controller (urls.py):

```
# For our show doodle type view
(r'^showDoodleType/(?P<theId>\d+)/$', showDoodleType),
```

Test by going to:

```
http://localhost:8000/showDoodleType/1/
```

...which should show something like :

```
Doodle Type Details
Id: 1
Name: Test Type 1
```

== Dealing with errors ==

One common error you may encounter is a url asking for a non existant object e.g.:

```
http://localhost:8000/showDoodleType/999/
```

You can use normal python error checking to deal with this, but django provides
a shortcut to deal with these situations in its aptly named shortcuts module.
Lets adapt our showDoodleType view to be a little more robust:

```
from django.shortcuts import get_object_or_404

def showDoodleType(theRequest, theId):
  # Old way:
  # myObject = DoodleType.objects.get(id=theId)
  # New way: 
  myObject = get_object_or_404(DoodleType, id=theId)
  myResult = "<h1>Doodle Type Details</h1>"
  myResult = myResult + "Id: " + str(myObject.id) + "<br />"
  myResult = myResult + "Name: " + str(myObject.name) + "<br />"
  return HttpResponse(myResult)
```

== Deleting an object ==

To your views.py add:

```
def deleteDoodleType(theRequest, theId):
  myObject = get_object_or_404(DoodleType, id=theId)
  myResult = "<h1>Doodle Type Deleted:</h1>"
  myResult = myResult + "Id: " + str(myObject.id) + "<br />"
  myResult = myResult + "Name: " + str(myObject.name) + "<br />"
  myObject.delete()
  return HttpResponse(myResult)
```

And to the urls.py add:

```
# For our delete doodle type view
(r'^deleteDoodleType/(?P<theId>\d+)/$', deleteDoodleType),
```

Then test:

```
http://localhost:8000/deleteDoodleType/1/
```

Result:

```
Doodle Type Deleted:
Id: 1
Name: Test
```

== Creating a model ==

To your views.py add:

```
def createDoodleType(theRequest, theName):
  myObject = DoodleType()
  myObject.name = theName
  myObject.save()
  myResult = "<h1>Doodle Type Created:</h1>"
  myResult = myResult + "Id: " + str(myObject.id) + "<br />"
  myResult = myResult + "Name: " + str(myObject.name) + "<br />"
  return HttpResponse(myResult)
```

And to the urls.py add:

```
# For our delete doodle type view
(r'^createDoodleType/(?P<theName>[a-zA-Z]+)/$', createDoodleType),
```

Then test:

```
http://localhost:8000/createDoodleType/Squiggle/
```

Result:

```
Doodle Type Created:
Id: 2
Name: Squiggle
```

== Last but not least, update a model ==


To your views.py add:

```
def updateDoodleType(theRequest, theId, theName):
  myObject = get_object_or_404(DoodleType, id=theId)
  myObject.name = theName
  myObject.save()
  myResult = "<h1>Doodle Type Updated:</h1>"
  myResult = myResult + "Id: " + str(myObject.id) + "<br />"
  myResult = myResult + "Name: " + str(myObject.name) + "<br />"
  return HttpResponse(myResult)
```

And to the urls.py add:

```
# For our update doodle type view
(r'^updateDoodleType/(?P<theId>\d+)/(?P<theName>[a-zA-Z]+)/$', updateDoodleType),
```

You will see above that we provide for two parameters to be passed to the URL -
first the id, and then the new name for the doodle.

Then test:

```
http://localhost:8000/updateDoodleType/2/Squaggle/
```

Result:

```
Doodle Type Created:
Id: 2
Name: Squaggle
```


== CRUD !==

Now we have crud facilities in our application!:

- **c**reate objects
- **r**ead objects
- **u**pdate objects
- **d**elete objects
-

CRUD is the basis for pretty much any data driven application so we are well on
our way to being able to create something useful.

== Now you try! ==

To see just how well you have grasped everything so far here is a little challenge:

```
1) Create a new model definition, sync it to the database.
2) Create controller rules to allow you to do CRUD with your model
3) Implement the view logic to support CRUD
4) Add a view method to show a listing of all your objects

and for bonus points

5) Create a controller rule and view method that will delete all 
   of your objects.
```

