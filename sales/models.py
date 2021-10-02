
from django.db import models
from rest_framework.fields import DateTimeField
from stock.models import Stock
from django.db.models import Sum
from datetime import datetime
from django.db.models import F



class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(unique=True)
    def paied(self):
        r= Payment.objects.filter(client=self.pk).aggregate(Sum('amount'))
        return r["amount__sum"] or 0
    def total(self):
        return Process.objects.filter(client=self.pk).aggregate(Sum('total'))["total__sum"] or 0
    def delais(self):
        d=Process.objects.filter(client=self.pk).filter(paied__lt=F('total')).order_by('date')

        if len(d): 
            return d[0].date
        else :
            return 'e'
    

    


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
    prix_final = models.IntegerField()
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
