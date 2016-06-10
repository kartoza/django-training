Advanced Users
==============

The user class can be very central to an application and you my find that
the standard out of the box model does not give enough functionality.

In this case you could either add a Profile or subclass the User model.


User Profile
------------

In this case you link a profile to a user account.

Create a profile::


    class UserProfile(models.Model):
        user = models.ForeignKey(User, unique=True)
        location = models.PointField()


Then configure in settings/project.py::

    AUTH_PROFILE_MODULE = 'demo_user.UserProfile'


This is great if you are happy with the standard user definition, but
only want to add some information.


Extending AbstractUser
----------------------


If you need to change the username type, or something else, that is core
to the user class, then the only option is to subclass. The auth module
provides us with a abstract class::


    from django.contrib.auth.models import AbstractBaseUser
    from django.contrib.gis.db import models

    from django.contrib.auth.models import AbstractUser


    class DemoUser(AbstractUser):
        type_choices = (
            ('Manager', 'Manager'),
            ('Agent', 'Agent'),
            ('Staff', 'Staff')
        )
        user_type = models.CharField(
            max_length=20,
            choices=type_choices,
            default='Staff')
        email = models.EmailField(max_length=70)

        first_name = models.CharField(
            verbose_name='First name',
            help_text='Your first name.',
            max_length=100,
            null=False,
            blank=False
        )

        last_name = models.CharField(
            verbose_name='Last name',
            help_text='Your last name.',
            max_length=100,
            null=False,
            blank=False
        )

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name', 'last_name']


Again we need to configure our app to actually take note of this and make
this the default user::

    AUTH_USER_MODEL = 'demo_user.User'


Exercise
--------

Create a demo_user app and create a demo user in there.(Hint: we need to
add this to installed apps.)
