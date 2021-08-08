
from django.db import models
from stock.models import Stock


class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(unique=True)


class Process(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey(
        Client, related_name='processes', on_delete=models.CASCADE, null=False, default=1)
    total = models.IntegerField()
    date = models.DateTimeField()
    paied = models.IntegerField()


class Payment(models.Model):
    client = models.ForeignKey(
        Client, related_name='payments', on_delete=models.CASCADE, null=False, default=1)
    amount = models.IntegerField()
    date = models.DateTimeField()
    process = models.ForeignKey(
        Process, related_name='payments', on_delete=models.CASCADE, null=False, default=1)


class Basket(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    date = models.DateTimeField()
    item_sale_price_final = models.IntegerField()
    process = models.ForeignKey(
        Process, related_name='baskets', on_delete=models.CASCADE, null=False, default=1)
    stock = models.ForeignKey(
        Stock, related_name='baskets', on_delete=models.CASCADE)


class Restore(models.Model):
    client = models.ForeignKey(
        Client, related_name='restores', on_delete=models.CASCADE, null=False, default=1)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()
    basket = models.ForeignKey(
        Basket, related_name='restores', on_delete=models.CASCADE, null=False, default=1)
