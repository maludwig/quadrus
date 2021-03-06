from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.views import generic
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.context_processors import csrf

from vehicles.models import *
import json

class IndexView(generic.ListView):
    model = Vehicle
    template_name = 'vehicles/index.html'

    def get_queryset(self):
        return Vehicle.objects.all()

def index_json(request):
    data = "["
    for v in Vehicle.objects.all():
        data += '{"make":"' + v.make + '","model":"' + v.model + '","description":"' + v.description + '","price":%i' % v.price + '},'
    data = data[0:len(data)-1] + "]"
    return HttpResponse(data)

@ensure_csrf_cookie
def orders(request):
    open_orders = Order.objects.filter(completed=False).order_by("order_date");
    completed_orders = Order.objects.filter(completed=True).order_by("-built_date");
    c = {
        "open_orders": open_orders,
        "completed_orders": completed_orders,
    }
    c.update(csrf(request))
    return render(request, "vehicles/orders.html", c)

def orders_json(request):
    open_orders = Order.objects.filter(completed=False).order_by("order_date");
    completed_orders = Order.objects.filter(completed=True).order_by("-built_date");
    oo_json = ""
    for oo in open_orders:
        oo_json += '{"id":"' + str(oo) + '","customer":"' + str(oo.customer) + '","vehicle":"' + str(oo.vehicle) + '","ordered":"' + str(oo.order_date) + '"},'
    oo_json = oo_json[0:len(oo_json)-1]
    co_json = ""
    for co in completed_orders:
        co_json += '{"id":"' + str(co) + '","customer":"' + str(co.customer) + '","vehicle":"' + str(co.vehicle) + '","ordered":"' + str(co.order_date) + '","built":"' + str(co.built_date) + '"},'
    co_json = co_json[0:len(co_json)-1]
    data = '{"open":[' + oo_json + '],"complete":[' + co_json + ']}'
    return HttpResponse(data)

@require_POST
def fill(request, pk):
    o = get_object_or_404(Order, pk=pk)
    o.completed = True
    o.built_date = timezone.now()
    o.save()
    return HttpResponseRedirect(reverse("vehicles:orders"))

@require_POST
def fill_json(request, pk):
    r = fill(request,pk)
    if(r.status_code != 404):
        return HttpResponseRedirect(reverse("vehicles:orders_json"))
    else:
        return r

@require_POST
def buy(request, pk):
    first = request.POST['first']
    last = request.POST['last']
    v = get_object_or_404(Vehicle, pk=pk)
    try:
        p = Person.objects.get(first_name=first, last_name=last)
    except (KeyError, Person.DoesNotExist):
        p = Person(first_name=first,last_name=last)
        p.save()
    o = Order(customer=p, vehicle=v, order_date=timezone.now())
    o.save()
    return HttpResponseRedirect(reverse("vehicles:orders"))

@require_POST
def buy_json(request, pk):
    r = buy(request,pk)
    if(r.status_code != 404):
        return HttpResponseRedirect(reverse("vehicles:orders_json"))
    else:
        return r
