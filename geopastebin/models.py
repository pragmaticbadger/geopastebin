from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry, GeometryCollection
import geojson, uuid


class PasteManager(models.Manager):
    def public(self):
        return self.get_query_set().filter(semi_private=False)

class Paste(models.Model):
    uuid = models.CharField(max_length=32, unique=True, db_index=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    paste = models.TextField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    semi_private = models.BooleanField(help_text=u'If checked your paste will not show on index pages but anyone who guesses the URL will be able to view it.')
    geom = models.GeometryCollectionField(blank=True, null=True)
    is_collection = models.BooleanField()

    objects = PasteManager()

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return u'Geopaste %s' % self.uuid

    def save(self, *args, **kwargs):
        if not self.pk:
            # Create a unique urlsafe base-64 encoded UUID4
            while 1:
                my_uuid = uuid.uuid4().hex
                try:
                    self.__class__.objects.get(uuid=my_uuid)
                except self.__class__.DoesNotExist:
                    self.uuid = my_uuid
                    break

        # Always update geom based on text but fail gracefully
        try:
            paste = self.paste
            # Preprocess GeoJSON Features and FeatureCollections
            if self.looks_like_geojson and self.looks_like_feature:
                paste = self.extract_geometries_from_features()
            geom = GEOSGeometry(paste)
            if geom.geom_type == 'GeometryCollection':
                # Store a GeometryCollection if that's what's provided
                self.geom = geom
                self.is_collection = True
            else:
                # Store within a GeometryCollection.
                self.geom = GeometryCollection(GEOSGeometry(self.paste))
        except:
            pass

        super(Paste, self).save(*args, **kwargs)

    @property
    def geometry(self):
        """If the paste has a geometry, return either the original stored within the
        GeometryCollection or a GeometryCollection if that's what the original paste
        was."""
        if not self.geom:
            return None
        if self.is_collection:
            return self.geom
        else:
            return self.geom[0]

    @models.permalink
    def get_absolute_url(self):
        return ('geopastebin_detail', [], {'slug' : self.uuid})

    def extract_geometries_from_features(self):
        geometries = []
        data = geojson.loads(self.paste)

        if data['type'] == 'FeatureCollection':
            for feature in data['features']:
                geometries.append(feature['geometry'])
        if data['type'] == 'Feature':
            geometries.append(data['geometry'])

        return geojson.dumps(geojson.geometry.GeometryCollection(geometries=geometries))

    @property
    def looks_like_geojson(self):
        if self.paste.count('{') + self.paste.count('}') + self.paste.count('[') + self.paste.count(']') > 2:
            return True
        else:
            return False

    @property
    def looks_like_feature(self):
        if self.paste.lower().count('feature') > 0:
            return True
        else:
            return False
