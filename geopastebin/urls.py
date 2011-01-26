from django.conf.urls.defaults import *

from geopastebin.models import Paste
from geopastebin.forms import PasteForm

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', kwargs={'queryset' : Paste.objects.public().order_by('-created'), 'paginate_by' : 20}),
    url(r'^create/', 'django.views.generic.create_update.create_object', kwargs={'form_class' : PasteForm}, name='geopastebin_create'),
    url(r'^(?P<slug>\w{32})/', 'django.views.generic.list_detail.object_detail', kwargs={'slug_field' : 'uuid', 'queryset' : Paste.objects.all()}, name='geopastebin_detail'),
)
