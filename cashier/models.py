
from sales.models import Basket, Client
from django.db import models
from stock.models import Brand, Soug, Stock


class Cashier(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()


class Log(models.Model):
    date = models.DateTimeField()
    profit = models.IntegerField()
    expance = models.IntegerField()
    credit = models.IntegerField()
    brand = models.ForeignKey(
        Brand, related_name='logs', on_delete=models.CASCADE)


class Expance(models.Model):
    name = models.CharField(max_length=200, null=True)
    details = models.TextField(blank=True)
    quantity = models.IntegerField()
    date = models.DateTimeField()
    amount = models.IntegerField()
    soug = models.ForeignKey(
        Soug, related_name='expances', on_delete=models.CASCADE)


class Diposite(models.Model):
    name = models.CharField(max_length=200, null=True)
    details = models.TextField(blank=True)
    quantity = models.IntegerField()
    date = models.DateTimeField()
    amount = models.IntegerField()


