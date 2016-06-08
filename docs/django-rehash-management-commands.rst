Management Commands
===================

Performing routine or once off functions is done by management commands. We
have encountered these before using the create superuser account::

    python manage.py createsuperuser

the code running here can be found in
``django/contrib/auth/management/commands``.

Management commands are all, by convention, found in
``{{ app_name }}/management/commands``. We will need to create these in our app.
once done we will need to use a bit of scaffolding. This is the following::

	from django.core.management import BaseCommand

		# The class must be named Command and subclass BaseCommand
		class Command(BaseCommand):
		# Show this when the user types help
		help = "New Command"

		# A command must define handle()
		def handle(self, *args, **options):
			""" Place our code here """

The name of the command is that of the filename.

Exercise
--------

Create a base command that creates creates 10 zones types and 1000
interest zones and randomly assigns them to the zones.

Hint::

     # Creating a polygon
     from django.contrib.gis.geos import Polygon
     Polygon(((1,2),(2,3),(2,4),(1,2)))
