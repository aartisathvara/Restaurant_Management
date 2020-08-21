from django.db import models

# Create your models here.
class Restaurent(models.Model):
    name = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=5000, null=True)
