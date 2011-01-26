from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import PasteForm
from django.http import HttpResponseRedirect

def create(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save()
            return HttpResponseRedirect(paste.get_absolute_url())
    else:
        form = PasteForm()
    
    return render_to_response('geopastebin/create.html', {
        'form' : form,
    }, context_instance=RequestContext(request))
