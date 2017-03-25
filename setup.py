"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='email_users',
    version='0.0.1',
    packages=['email_users', 'email_users.migrations'],
    url='https://bitbucket.org/poirier/email_users',
    license='',
    author='poirier',
    author_email='',
    description=''
)
