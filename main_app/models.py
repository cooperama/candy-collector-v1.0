from django.db import models
from django.urls import reverse #
from django.contrib.auth.models import User


class Candy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.IntegerField()
    in_stock = models.BooleanField()

    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
