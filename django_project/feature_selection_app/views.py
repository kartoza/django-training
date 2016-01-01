from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    render_to_response)
from django.template import RequestContext

from feature_selection_app.models import DoodleType
from feature_selection_app.models import Doodle
from feature_selection_app.forms import DoodleForm


def helloWorld(theRequest):
    """A simple hello world view"""
    if theRequest.user.username == 'timlinux':
        return HttpResponse('Dude you are awesome!')
    else:
        return HttpResponse('<h1>Hello World</h1>')


def menu(theRequest):
    """Create menu"""
    myMenu = '<h1>Menu</h1>'
    myMenu += '<a href="/doodle/listDoodleTypes/">List Doodle Types</a>'
    return HttpResponse(myMenu)


def hello(theRequest, thePerson):
    """A view that prints a person's name"""
    return HttpResponse("<h1>Hello " + str(thePerson) + "</h1>")


def listDoodleTypes(theRequest):
    """A view to show all doodle types"""
    myObjects = DoodleType.objects.all().order_by("-name")
    myDoodle = Doodle.objects.get(id=1)
    return render_to_response('doodleTypesList.html',
                              {'myObjects': myObjects,
                               'myDoodle': myDoodle})


def listDoodles(theRequest):
    """A view to show all doodle types"""
    myObjects = Doodle.objects.all().order_by("-name")
    return render_to_response('doodleList.html',
                              {'myObjects': myObjects})


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


def createDoodleType(theRequest, theName):
    """Create a doodle type given a name"""
    myObject = DoodleType()
    myObject.name = theName
    myObject.save()
    myResult = "<h1>Doodle Type Created:</h1>"
    myResult = myResult + "Id: " + str(myObject.id) + "<br />"
    myResult = myResult + "Name: " + str(myObject.name) + "<br />"
    return HttpResponse(myResult)


def updateDoodleType(theRequest, theId, theName):
    myObject = get_object_or_404(DoodleType, id=theId)
    myObject.name = theName
    myObject.save()
    myResult = "<h1>Doodle Type Updated:</h1>"
    myResult = myResult + "Id: " + str(myObject.id) + "<br />"
    myResult = myResult + "Name: " + str(myObject.name) + "<br />"
    return HttpResponse(myResult)


def doodleForm(theRequest, theId=None):
    myForm = None
    myObject = None
    if theId:
        myObject = get_object_or_404(Doodle, id=theId)
    if theRequest.method == 'POST':
        if myObject:
            myForm = DoodleForm(theRequest.POST, instance=myObject)  # editing
        else:
            myForm = DoodleForm(theRequest.POST)  # submit new
        if myForm.is_valid():
            myObject = myForm.save()
            return render_to_response("doodleForm.html",
                                      {"myDoodle": myObject})
    else:
        if theId:
            myForm = DoodleForm(instance=myObject)
        else:
            myForm = DoodleForm()

    return render_to_response(
      "doodleForm.html",
      {
        "myForm": myForm,
        "myObjectId": theId,
      },
      context_instance=RequestContext(theRequest),
      mimetype='text/html'
    )
