Developing using Eclipse (Linux)
================================


This section outlines how you can set up Eclipse with PyDev to work on an
existing Django aplication. The benifits? A complete IDE environment with a
debugger that will let you set breakpoints anywhere in your app and
interactively step through the code from that point.  You also get other nice
things like refactoring support, code completion and so on. 

.. note:: This is optional - you can use any environment you like for editing
   python, or even a simple text editor.

Install Eclipse
------------------

Under ubuntu you can simply do::
  
   sudo apt-get install eclipse

Install PyDev
-------------

.. note:: These steps are also explained in the PyDev documentation which is
   quite good.
   
First you need to do :menuselection:`Help->Install New Software`. Then click on the
:guilabel:`Add` button and fill in the details as shown below:

Add the PyDev extensions (click for larger image)

Next choose the PyDev and PyDev Extensions item from the 'work with' list and
wait a moment. Then tick :guilabel:`PyDev` from the software list and untick
:guilabel:`Contact all update sites to find required software`. Then click
:guilabel:`next` and wait while the packages download.

After you are done, click :guilabel:`finish` to close the installer and restart
Eclipse as prompted.

Setup your project
------------------

Choose the :guilabel:`PyDev source` and select :guilabel:`PyDev` from the list.
We are going to use our existing Django web site you want to work with, but
note that the PyDev will also happily create a new Django project from scratch
for you.

This is a 'broad strokes' outline of the process:

- create a new django project in your Eclipse project workspace named the same
  as your existing project
- remove the project director and replace it with a symlink to your real project
- setup Eclipse to be aware of our virtualenv
- set breakpoints, run the development server and generally have fun with
  Django within an IDE

So, first up, open Eclipse and use a workspace (I took the default one as shown
below):

Open a workspace (click for larger image)

Next, create a new Django project: :menuselection:`File -> New -> Project`....
and then choose PyDev Django Project from the dialog that appears.


 Create a new django project (click for larger image)

Click :guilable:`next` and then you should give the project the same name as
the existing Django project that you want to bring into Eclipse (in our case
django-project). Also choose :guilable:`don't configure PYTHONPATH` from the
options in the dialog that appears:


 Configure your project (click for larger version)
  

Use the hyperlink on the above dialog to configure your python interpreter. On
the screen that appears we get to tell PyDev where our virtual environment is.
Click :guilabel:`New` then fill the interpreter details in like this:


 Point pydev to your virtual environment (click for larger version)
  

When you click :guilabel:`OK`, a dialog like this will appear, and you should
enable the system python ('/usr/lib/python2.7' in my case) too.


Configured python interpreter dialog (click for larger view)

Clicking :guilabel:`OK` will take you back to the Eclipse preferences window
and should look something like this:


 Final view of Eclipse preferences (click for larger view)

Now click OK and it will start doing some magic stuff, eventually bringing you
back to the 'PyDev Django Project' dialog. Be sure to change the interpreter
option to :guilabel:`Django-Training VirtualEnvironment` (or similar based on
your previous choices). Click :guilabel:`next` and you will be prompted for
your database connection details. You can completely ignore this since we will
be grafting in the settings from our existing 'django-project' project below. So
clicking :guilabel:`Finish` will end this part of the process.

You may need to press F5 to refresh the project view before you see all your
real project files. Good so now we have our project all set up in Eclipse it
should look something like this:

  
Our django project loaded in Eclipse (click for larger image)
  

Debugging
---------

The last part of this article covers debugging. The process is really simple.
First open a source file (for example :file:`doodle-app/views.py`) and then
double click in a margin where you would like to place a break point.


Setting a breakpoint in your project (click for larger image)
  

Next you can run the django development server  by right clicking on the
project and from the context menu choosing :menuselection:`Debug As --> PyDe :
Django`.


Launching the debugger (click for larger image)
  

PyDev will prompt you to switch to the debug perspective. Now you can go ahead
and open the site in your browser. When you hit the url that triggers the
breakpoint, PyDev will stop, highlight the line and you can use the normal
debugging tools for there on. You can view the state of any variable while
django is running and so on.


Debugging your Django application interactively - woohoo! (Click for larger image)
  

Creating a project
..................

The procedure for doing this is to do:
:menuselection:`File --> New --> Project...` and
then from the resulting dialog do :menuselection:`PyDev --> PyDev Project`.

In the resulting project dialog, set the following details:

* :guilabel:`Project name:` : :kbd:`inasafe`
* :guilabel:`Use default` : :kbd:`uncheck`
* :guilabel (linux):`Directory` : :kbd:`/home/<your user name/.qgis/python/plugins/inasafe/`
* :guilabel (windows):`Directory` : :kbd:`/home/<your user name/.qgis/python/plugins/inasafe/`
* :guilabel:`Choose project type` : :kbd:`Python`
* :guilabel:`Grammar Version` : :kbd:`2.7`
* :guilabel:`Add project directory to PYTHONPATH?` : :kbd:`check`

At this point you should should click the link entitled 'Please configure an interpreter
in related preferences before continuing.' And on the resulting dialog do:

* :guilabel:`Python Interpreters: New...` : :kbd:`click this button`

In the dialog that appears do:

* :guilabel:`Interpreter Name` : :kbd:`System Python 2.7`
* :guilabel:`Interpreter Executable` : :kbd:`/usr/bin/python`
* :guilabel:`OK Button` : :kbd:`click this button`

Another dialog will appear. 

* :guilabel:`OK Button` : :kbd:`click this button`

You will be returned to the Python Interpreters list and should see an entry for
System Python 2.7 listed there. Now do in the *Libraries* tab:

* :guilabel:`Finish` : :kbd:`click this button`



Running Unit tests from the IDE
...............................

Python has very good integrated support for unit testing. The first thing
you should do after setting up the IDE project is to run the tests. You can run tests
in the following ways:






