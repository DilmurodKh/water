from django.db import models

# Create your models here.
class WaterModel(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    createdate = models.TimeField(auto_now_add=True)
    telnumber = models.CharField(max_length=13)
    quantity = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.name
