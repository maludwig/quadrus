from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.views import generic
from vehicles.models import *
import json

class IndexView(generic.ListView):
    model = Vehicle
    template_name = 'vehicles/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Vehicle.objects.all()

def index_json(request):
    data = "["
    for v in Vehicle.objects.all():
        data += '{"make":"' + v.make + '","model":"' + v.model + '","description":"' + v.description + '","price":%i' % v.price + '},'
    data = data[0:len(data)-1] + "]"
    return HttpResponse(data)
