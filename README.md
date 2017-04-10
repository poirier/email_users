email_users
===========

A replacement for the Django User class that uses email addresses
as the primary identifier, and does away with usernames.

Note: The Django docs strongly recommend, and I concur, that if you're going
to use a custom user model in your project, you use it from the start. You
can extend it later much more easily than you can switch to a different one.

Therefore, this package only provides an abstract model, which you should use
as a parent class for your own User model, even if you don't customize it at all for now.

See https://docs.djangoproject.com/en/stable/topics/auth/customizing/#auth-custom-user
for more about using alternative User models in Django.

Requirements:

* Django (only tested with Django 1.10 so far)
* Python 3.x

To use this as a base class for your own user class:

1. Install in your Django project's virtualenv:

    pip install git+https://bitbucket.org/poirier/email_users

2. Create your own user model that inherits from the abstract version of this one:

    from django.db import models
    from email_users import AbstractEmailUser
    
    class MyUser(AbstractEmailUser):
        pass

3. Add your own user model as AUTH_USER_MODEL in settings:

    AUTH_USER_MODEL = 'myapp.MyUser'
