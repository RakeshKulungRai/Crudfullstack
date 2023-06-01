from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length =225)
    address = models.CharField(max_length = 225)
    fee = models.IntegerField()
