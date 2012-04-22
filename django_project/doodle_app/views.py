from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from models import DoodleType


def helloWorld(theRequest):
    """A simple hello world view"""
    return HttpResponse('<h1>Hello World</h1>')


def hello(theRequest, thePerson):
    """A view that prints a person's name"""
    return HttpResponse("<h1>Hello " + str(thePerson) + "</h1>")


def listDoodleTypes(theRequest):
    """A view to show all doodle types"""
    myObjects = DoodleType.objects.all()
    # Optional - sort descending:
    #myObjects = DoodleType.objects.all().order_by("-name")
    myResult = "<h1>doodle types</h1>"
    for myObject in myObjects:
        myResult = (myResult + str(myObject.id) +
                   ' : ' + str(myObject.name) + '<br />')
    return HttpResponse(myResult)


def showDoodleType(theRequest, theId):
    """Show a doodle type given it's id"""
    myObject = get_object_or_404(DoodleType, id=theId)
    myResult = "<h1>Doodle Type Details</h1>"
    myResult = myResult + "Id: " + str(myObject.id) + "<br />"
    myResult = myResult + "Name: " + str(myObject.name) + "<br />"
    return HttpResponse(myResult)


def deleteDoodleType(theRequest, theId):
    """Delete a doodle type given its id"""
    myObject = get_object_or_404(DoodleType, id=theId)
    myResult = "<h1>Doodle Type Deleted:</h1>"
    myResult = myResult + "Id: " + str(myObject.id) + "<br />"
    myResult = myResult + "Name: " + str(myObject.name) + "<br />"
    try:
        myObject.delete()
    except Exception, e:
        myResult = '<b>Error:</b>' + str(e)
    return HttpResponse(myResult)
