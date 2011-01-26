from django.contrib.gis.geos import GEOSGeometry
from django.test import TestCase

class PasteTestCase(TestCase):
    
    def test_full_form(self):
        ll = (-95.2164722, 39.0111111)
        data = {
            'title' : u'This is my title',
            'paste' : u'POINT(%s %s)' % ll,
            'description' : u'This is my description.,',
            'semi_private' : True,
        }
        # Post the data
        response = self.client.post('/create/', data)
        # A 302 is issued upon successful save
        self.assertEqual(response.status_code, 302)
        # Get the detail page for the newly created object
        response = self.client.get(response['Location'])
        # Ensure that we get back what we put in
        paste = response.context[-1]['object']
        self.assertEqual(paste.title, data['title'])
        self.assertEqual(paste.paste, data['paste'])
        self.assertEqual(paste.description, data['description'])
        self.assertEqual(paste.semi_private, data['semi_private'])
        # Ensure that the geometry parsed correctly
        geom_ll = paste.geometry.get_coords()
        self.assertAlmostEqual(geom_ll[0], ll[0])
        self.assertAlmostEqual(geom_ll[1], ll[1])

JSON_TESTS = [
    """{ "type": "Point", "coordinates": [100.0, 0.0] }""",
    """{ "type": "LineString",
      "coordinates": [ [100.0, 0.0], [101.0, 1.0] ]}""",
    """{ "type": "Polygon",
        "coordinates": [
          [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]
          ]}""",
    """{ "type": "Polygon",
         "coordinates": [
           [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ],
           [ [100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2] ]
           ]}""",
    """{ "type": "MultiPoint",
         "coordinates": [ [100.0, 0.0], [101.0, 1.0] ]}""",
    """{ "type": "MultiLineString",
         "coordinates": [
               [ [100.0, 0.0], [101.0, 1.0] ],
               [ [102.0, 2.0], [103.0, 3.0] ]
             ]}""",
    """{ "type": "MultiPolygon",
          "coordinates": [
            [[[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]],
            [[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
             [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]]]
            ]}""",
    """{ "type": "GeometryCollection",
         "geometries": [
           { "type": "Point",
             "coordinates": [100.0, 0.0]
             },
           { "type": "LineString",
             "coordinates": [ [101.0, 0.0], [102.0, 1.0] ]
             }
         ]}""",
]

JSON_FEATURE = """{ "type": "Feature",
  "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
  "properties": {"prop0": "value0"}
  }"""

JSON_FEATURE_GEOMETRY = """{"type": "Point", "coordinates": [102.0, 0.5]}"""

JSON_FEATURECOLLECTION = """{ "type": "FeatureCollection",
  "features": [
    { "type": "Feature",
      "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
      "properties": {"prop0": "value0"}
      },
    { "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
          ]
        },
      "properties": {
        "prop0": "value0",
        "prop1": 0.0
        }
      }
     ]
   }"""

JSON_FEATURECOLLECTION_GEOMETRY = """{"type" : "GeometryCollection",
                                      "geometries" : [
                                        {"type": "Point", "coordinates": [102.0, 0.5]},
                                        {
                                            "type": "LineString",
                                            "coordinates": [
                                              [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
                                              ]
                                        }]}"""

class GeoJSONTestCase(TestCase):
    def test_json(self):
        for json_test in JSON_TESTS:
            # Post the data
            response = self.client.post('/create/', {'paste' : json_test})
            self.assertEqual(response.status_code, 302)
            response = self.client.get(response['Location'])
            paste = response.context[-1]['object']
            # Ensure that we get back what we put in
            self.assert_(paste.geometry.equals(GEOSGeometry(json_test)))

    def test_feature(self):
        response = self.client.post('/create/', {'paste' : JSON_FEATURE})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response['Location'])
        paste = response.context[-1]['object']
        # Ensure that we get back what we put in
        self.assert_(paste.geometry.equals(GEOSGeometry(JSON_FEATURE_GEOMETRY)))

    def test_featurecollection(self):
        response = self.client.post('/create/', {'paste' : JSON_FEATURECOLLECTION})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(response['Location'])
        paste = response.context[-1]['object']
        # Ensure that we get back what we put in
        self.assert_(paste.geometry.equals(GEOSGeometry(JSON_FEATURECOLLECTION_GEOMETRY)))