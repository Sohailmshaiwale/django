from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)  # 2083 is the std length of the url


class Offer(models.Model):
    code = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    discount = models.FloatField()