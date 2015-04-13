from django.db import models
import locale
# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=200, default="Lexus")
    model = models.CharField(max_length=200)
    image = models.ImageField(upload_to="vehicles")
    description = models.TextField()
    price = models.IntegerField()
    HYBRID = "H"
    GAS = "G"
    ELECTRIC = "E"
    TYPE_CHOICES = (
        (HYBRID, 'hybrid'),
        (GAS, 'gas'),
        (ELECTRIC, 'electric'),
    )
    TYPE_ICONS = {
        "H": "leaf",
        "G": "tint",
        "E": "bolt",
    }
    type = models.CharField(max_length=1,choices=TYPE_CHOICES,default=GAS)
    def __unicode__(self):
        return self.make + " - " + self.model
    def formatted_price(self):
        return "${:,.2f}".format(self.price);
    def icon(self):
        # return "ICON"
        return self.TYPE_ICONS[self.type];

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Order(models.Model):
    customer = models.ForeignKey(Person)
    vehicle = models.ForeignKey(Vehicle)
    order_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    built_date = models.DateTimeField(blank=True,null=True)
    def __unicode__(self):
        return "%04i" % self.pk
