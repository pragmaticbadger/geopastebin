from django.contrib.gis.geos import GEOSGeometry, GeometryCollection
from django.contrib.gis.gdal.error import OGRException
from django.forms import ModelForm, ValidationError
from models import Paste

class PasteForm(ModelForm):
    class Meta:
        model = Paste
        exclude = ('uuid', 'geom', 'is_collection')
