from django.test import TestCase
from models import Doodle
from models import DoodleType
from django.test.client import RequestFactory
from views import helloWorld
from views import hello
from views import showDoodleType
from views import createDoodleType
from django.test.client import Client
from django.http import Http404


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
        myRequest = self.factory.get('/doodle/helloWorld')
        myResponse = helloWorld(myRequest)
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = '<h1>Hello World</h1>'
        myMessage = ('Unexpected response from helloWorld'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)

    def testHelloWorldUrl(self):
        """Test that the helloWorld url works using the django test web client.
        """
        myClient = Client()
        myResponse = myClient.get('/doodle/helloWorld/')
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = '<h1>Hello World</h1>'
        myMessage = ('Unexpected response from helloWorld URL'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)

    def testHelloTimView(self):
        """Test hello tim view works."""
        myRequest = self.factory.get('/doodle/hello/Tim')
        myResponse = hello(myRequest, 'Tim')
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = '<h1>Hello Tim</h1>'
        myMessage = ('Unexpected response from hello'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)

    def testHelloTimUrl(self):
        """Test that the hello tim url works using the django test web client.
        """
        myClient = Client()
        myResponse = myClient.get('/doodle/hello/Tim/')
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = '<h1>Hello Tim</h1>'
        myMessage = ('Unexpected response from helloWorld URL'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)

    def testListDoodleTypesView(self):
        """Test list doodle types view works."""
        myRequest = self.factory.get('/doodle/hello/Tim')
        myResponse = hello(myRequest, 'Tim')
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = '<h1>Hello Tim</h1>'
        myMessage = ('Unexpected response from hello'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)

    def testListDoodleTypesUrl(self):
        """Test list doodle types using the django test web client.
        """
        myClient = Client()
        myResponse = myClient.get('/doodle/listDoodleTypes/')
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = ('<h1>doodle types</h1>1 : Big<br />'
                            '2 : Medium<br />3 : Small<br />')
        myMessage = ('Unexpected response from helloWorld URL'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)

    def testShowDoodleTypeView(self):
        """Test show single doodle type view works."""
        myRequest = self.factory.get('/doodle/showDoodleType/1/')
        myResponse = showDoodleType(myRequest, 1)
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = ('<h1>Doodle Type Details</h1>Id: 1'
                            '<br />Name: Big<br />')
        myMessage = ('Unexpected response from hello'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)

    def testShowDoodleTypeUrl(self):
        """Test show single doodle type url works.
        """
        myClient = Client()
        myResponse = myClient.get('/doodle/showDoodleType/1/')
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = ('<h1>Doodle Type Details</h1>Id: 1'
                            '<br />Name: Big<br />')
        myMessage = ('Unexpected response from helloWorld URL'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)

    def testInvalidShowDoodleTypeView(self):
        """Test show invalid single doodle type view returns 404"""
        try:
            myRequest = self.factory.get('/doodle/showDoodleType/999/')
            showDoodleType(myRequest, 999)
        except Http404:
            pass
        except:
            assert()

    def testInvalidShowDoodleTypeUrl(self):
        """Test show single invlalid doodle type url returns 404.
        """
        myClient = Client()
        myResponse = myClient.get('/doodle/showDoodleType/999/')
        self.assertEqual(myResponse.status_code, 404)

    def testCreateDoodleTypeView(self):
        """Test create single doodle type view works."""
        myRequest = self.factory.get('/doodle/createDoodleType/SuperDoodle/')
        myResponse = createDoodleType(myRequest, 'SuperDoodle')
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = ('<h1>Doodle Type Created:</h1>Id: 4<br />'
                            'Name: SuperDoodle<br />')
        myMessage = ('Unexpected response from hello'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)

    def testCreateDoodleTypesUrl(self):
        """Test create doodle type using a url.
        """
        myClient = Client()
        myResponse = myClient.get('/doodle/createDoodleType/SuperDoodle/')
        self.assertEqual(myResponse.status_code, 200)
        myExpectedString = ('<h1>Doodle Type Created:</h1>Id: 4<br />'
                            'Name: SuperDoodle<br />')
        myMessage = ('Unexpected response from helloWorld URL'
                     ' - got %s, expected %s' %
                     (myResponse.content, myExpectedString))
        self.assertEqual(myResponse.content, myExpectedString, myMessage)
