# Create your views here.
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from location.models import Location

def view_location_list(request):
    
    d = { 'locations' : Location.objects.all()\
        ,'title' : 'Restroom Location Finder'\
     }
     
    return render_to_response('location/view_location_list.html', d, context_instance=RequestContext(request))
    
    return HttpResponse("Hello, world. You're at the poll index.")