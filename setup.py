import os
from setuptools import setup, find_packages

install_requires = []

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.markdown')

description = 'Some Django middleware to provide SSL redirection.'

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description


setup(
    name='django-watersheep',
    version='0.9.0',
    install_requires=install_requires,
    description=description,
    long_description=long_description,
    author='Dumbwaiter Design',
    author_email='dev@dwaiter.com',
    url='http://bitbucket.org/dwaiter/django-watersheep/',
    packages=['watersheep'],
)
