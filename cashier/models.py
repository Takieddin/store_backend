
from sales.models import Basket, Client
from django.db import models
from stock.models import Brand, Soug, Stock
from django.db.models import Sum


class Cashier(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()

    def sum(self):
        return Cashier.objects.aggregate(Sum('amount'))


class Coffre(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()

    def sum(self):
        return Coffre.objects.aggregate(Sum('amount'))


class Withdraw(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()

    def sum(self):
        return Withdraw.objects.aggregate(Sum('amount'))


class Profit(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()
    brand = models.ForeignKey(
        Brand, related_name='profits', on_delete=models.CASCADE,null=True)

    def sum(self):
        return Withdraw.objects.aggregate(Sum('amount'))


class Credit(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()

    def sum(self):
        return Withdraw.objects.aggregate(Sum('amount'))


class SaleProfit(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()

    def sum(self):
        return Withdraw.objects.aggregate(Sum('amount'))


class Brandlog(models.Model):
    brand = models.ForeignKey(
        Brand, related_name='logs', on_delete=models.CASCADE)
    date = models.DateTimeField()


class Log(models.Model):
    date = models.DateTimeField()
    profit = models.IntegerField()
    credit = models.IntegerField()
    sale_profit = models.IntegerField()

    def sum_profit(self):
        return Withdraw.objects.aggregate(Sum('profit'))

    def sum_credit(self):
        return Withdraw.objects.aggregate(Sum('credit'))

    def sum_sale_profit(self):
        return Withdraw.objects.aggregate(Sum('sale_profit'))


class Expance(models.Model):
    name = models.CharField(max_length=200, null=True)
    details = models.TextField(blank=True)
    date = models.DateTimeField()
    amount = models.IntegerField()

    def sum(self):
        return Withdraw.objects.aggregate(Sum('amount'))


class Diposite(models.Model):

    name = models.CharField(max_length=200, null=True)
    details = models.TextField(blank=True)
    date = models.DateTimeField()
    amount = models.IntegerField()
