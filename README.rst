===========
Geopastebin
===========

A simple BSD-licensed Django application for sharing GIS-related pastes such as
WKT, EWKT, and GeoJSON.

Getting started
===============

To run the example project, make sure that you have the requirements below.

Then::

    $ cd example_project
    $ createdb -T template_postgis geopastebin
    $ ./manage.py syncdb
    $ ./manage.py runserver

If you would like to override any settings, create a ``local_settings.py``
file in example_project.  For example, to override the database name::

    from settings import *
    
    DATABASES['default]['NAME'] = 'mygeopastebin'

You can also include Geopastebin in your own project by adding it to
``urls.py``::

    urlpatterns = patterns('',
    ...
    (r'^geopastebin/', include('geopastebin.urls')),
    )

Geopastebin also has basic test coverage::

    $ ./manage.py test geopastebin --verbosity=0
    ----------------------------------------------------------------------
    Ran 4 tests in 0.323s

    OK

Requirements
============

* `Django`_ 1.2.4 or `1.2.X release branch`_. Older versions may work
  but are untested.
* `PostGIS`_
* `psycopg2`_
* `geojson`_
* `django-olwidget`_

To Do
=====

* Store created paste uuid in session and allow that user to edit.
* Allow login for editing and keeping track of pastes?
* Give users the option of using olwidget to create or edit their paste.
* Live preview before submit using olwidget.
* Give users control over map display (zoom, etc).
* Determine how to license user-generated content.

Known bugs
==========

* Does not support KML
* Other formats to consider: NMEA, GML, GPX

.. _Django: http://www.djangoproject.com/
.. _1.2.X release branch: http://code.djangoproject.com/svn/django/branches/releases/1.2.X/
.. _PostGIS: http://postgis.refractions.net/
.. _psycopg2: http://pypi.python.org/pypi/psycopg2
.. _geojson: http://pypi.python.org/pypi/geojson
.. _django-olwidget: http://pypi.python.org/pypi/django-olwidget
