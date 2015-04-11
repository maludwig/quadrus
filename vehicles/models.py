from django.db import models
import locale
# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=200, default="Lexus")
    model = models.CharField(max_length=200)
    image = models.ImageField(upload_to="vehicles")
    description = models.TextField()
    price = models.IntegerField()
    def __unicode__(self):
        return self.make + " - " + self.model
    def formatted_price(self):
        return "${:,.2f}".format(self.price);
