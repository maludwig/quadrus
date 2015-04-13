from django.contrib import admin
from vehicles.models import *
# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Person)

class PersonInline(admin.TabularInline):
    model = Person

class VehicleInline(admin.TabularInline):
    model = Vehicle

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)
