===========
Geopastebin
===========

A simple BSD-licensed Django application for sharing GIS-related pastes such as
WKT, EWKT, and GeoJSON.

Getting started
===============

To run the example project, make sure that ``geopastebin``, ``olwidget``,
``geojson`` and ``django 1.2`` are on your ``PYTHONPATH`` and you have
``PostGIS`` installed.

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
