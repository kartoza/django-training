
   createdb django_project
   createlang plpgsql django_project
   psql django_project < /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
   psql django_project < /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql

.. note:: If you are using a different version of postgresql those last two
   lines should be adjusted accordingly.

Setup your Database connection
------------------------------

At this point you should fill in the database connection settings (in settings.py)::

   # Note delete django.db.backends.
   DATABASE_ENGINE = 'postgresql_psycopg2'
   DATABASE_NAME = 'django_project'
   DATABASE_USER = 'foouser'
   DATABASE_PASSWORD = 'foopassword'
   DATABASE_HOST = 'localhost'
   DATABASE_PORT = '5432'
