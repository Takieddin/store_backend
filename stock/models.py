from django.db import models
from django.db.models import Sum
from datetime import datetime



class Category(models.Model):
    name = models.CharField(max_length=200)


class Brand(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, related_name='brands', on_delete=models.CASCADE,null=True)


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(unique=True)
    def total(self):
        r= Stock.objects.filter(supplier=self.pk).aggregate(Sum('item_buying_price'))or 0
        return r["item_buying_price__sum"] or 0
    def paied(self):
        return Clearance.objects.filter(supplier=self.pk).aggregate(Sum('amount'))["amount__sum"]or 0
    def delais(self):
        d=Clearance.objects.filter(supplier=self.pk).order_by('date')
        print(d)

        if len(d): 
            return d[0].date
        else :
            return datetime.now()



    

class Soug(models.Model):
    name = models.CharField(max_length=200)
    note = models.TextField(blank=True)
    date = models.DateTimeField()
    total = models.IntegerField()
    paied = models.IntegerField()


class Stock(models.Model):
    name = models.CharField(max_length=200)
    note = models.TextField(blank=True)
    quantity = models.IntegerField()
    date = models.DateTimeField()
    item_buying_price = models.IntegerField()
    item_sale_price = models.IntegerField()
    instock = models.IntegerField()
    supplier = models.ForeignKey(
        Supplier, related_name='stocks', on_delete=models.CASCADE, null=False, default=1)
    
    brand = models.ForeignKey(
        Brand, related_name='stocks', on_delete=models.CASCADE)

class Clearance(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()
    supplier = models.ForeignKey(
        Supplier, related_name='clearances', on_delete=models.CASCADE)
    stock = models.ForeignKey(
        Stock, related_name='clearances', on_delete=models.CASCADE)
