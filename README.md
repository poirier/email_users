email_users
===========

A replacement for the Django User class that uses email addresses
as the primary identifier, and does away with usernames.

Note: The Django docs strongly recommend, and I concur, that if you're going
to use a custom user model in your project, you use it from the start. You
can extend it later much more easily than you can switch from the default
model to a different one.

See https://docs.djangoproject.com/en/stable/topics/auth/customizing/#auth-custom-user
for more about using alternative User models in Django.

Requirements:

* Django (only tested with Django 1.10 so far)
* Python 3.x

To use:

1. Install in your Django project's virtualenv:

    pip install git+https://bitbucket.org/poirier/email_users

2. Add to INSTALLED_APPS in settings:

    INSTALLED_APPS = [
        ...
        'email_users',
    ]

3. Set AUTH_USER_MODEL in settings:

    AUTH_USER_MODEL = 'email_users.EmailUser'

