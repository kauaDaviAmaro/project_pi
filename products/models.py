from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    is_active = models.BooleanField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    options = models.JSONField(null=True, blank=True)