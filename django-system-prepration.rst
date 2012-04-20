System Preparation
==================

Creating the top level working dir
----------------------------------

Django is available in apt, but this will be one of the few times I break my
rule about preferring apt installed packages over hand installed.

Instead we will use something called a 'python virtual environment' * which is 
considered to be the best practice for deploying a django project.

We will begin by creating a top level working directory e.g.::

   mkdir -p /home/web/django-training
   cd /home/web/django-training


Understanding the directory structure
-------------------------------------

In our next step we will set up our virtual environment. We are aiming to end up 
with something like this::

   django-training
   |-- project1
   |   |-- app1
   |   `-- app2
   |-- project2
   |   |-- app1
   |   `-- app2
   `-- python   <-- virtual environment for python

Django divides your work into projects and applications. A **project** provides 
shared templates, media (images, logos etc) to its applications and a shared
user database and so on.

An **application** provides some specific functionality. You can also install 
third party applications under your project directory to provide things like 
login frameworks etc.

We will get on to how projects and applications are created in a minute, but first 
lets get our python virtual environment set up...

Creating the virtual environment
--------------------------------

To create your virtual environment (and install a few other dependencies)  make
sure you are in the 
django directory we created above first and then do::

   sudo apt-get install python-setuptools build-essential python-dev libpq-dev
   sudo easy_install virtualenv
   virtualenv --no-site-packages python
   source python/bin/activate
   easy_install pip  <-- newer virtual env may do this automatically
          

What have we just done? We have set up a virtual environment (think of it 
as a simplified version of a virtual machine). In the virtual environment,
we have a repeatable, easily backed up and independent set of python 
libraries used to drive the django web site we are going to create.

+ **Repeatable** : you can easily deploy your application to another machine
+ **Easily backed up** : you just backup the whole of your django dir and
  then you have a backup of not only your django project, but also 
  the python libs needed to run it.
+ **Independent** : If the system libraries change, it should not affect 
     your web site.

Install Django into the Virtual Environment
-------------------------------------------


Now we want to install django and a few other pre-requisites into the 
virtual environment::

   pip install django
   pip install django-registration
   pip install django-debug-toolbar
   pip install django-extensions
   pip install psycopg2
   pip install ipython


You need to be connected to the internet for the above commands to work. 
The above commands install django, psycopg2 (which lets python connect to 
postgresql databases) and a few other useful django applications which 
we will use later in this tutuorial.

In case you are wondering, pip is a package management tool for python.

.. tip:: You can view the pip installed package in your virtual environment by
   doing :command:`pip freeze`

Following the above steps, your directory structure should now look like this::

   django-training
   `-- python
       |-- bin
       |   |-- activate
       |   |-- activate_this.py
       |   |-- django-admin.py
       |   |-- easy_install
       |   |-- easy_install-2.6
       |   |-- pip
       |   `-- python
       |-- include
       |   `-- python2.7 -> /usr/include/python2.7
       `-- lib
           `-- python2.7


Activate the virtual env
------------------------

Whenever you start a shell session, you need to source the activate script to
enabled the python virtual environment::

   source python/bin/activate

This sets up the system search path for python to look into your virtual env. 
in preference over using the system libs under /usr/lib/python.

Setup Postgresql
----------------

You don't need to use postgresql with django - it supports a variety of 
other databases. But its a good choice for a backend especially in light 
of the support for spatial datasets via PostGIS, so lets install and use it::
   
   sudo apt-get install postgresql-9.1-postgis

