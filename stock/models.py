from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=200)

class Brand(models.Model):
    name = models.CharField(max_length=200)    
    category = models.ForeignKey(Category, related_name='brands', on_delete=models.CASCADE)
class Supplier(models.Model):
    name = models.CharField(max_length=200)    
    phone = models.IntegerField(unique=True)
class Soug(models.Model):
    name = models.CharField(max_length=200)
    note = models.TextField(blank=True)
    date =models.DateField()
    total=models.IntegerField()
    paied =models.IntegerField()
    
class Stock(models.Model):
    name = models.CharField(max_length=200)
    note = models.TextField(blank=True)
    quantity  = models.IntegerField()
    date =models.DateField()
    item_buying_price = models.IntegerField()
    item_sale_price = models.IntegerField()
    instock=models.IntegerField()
    supplier = models.ForeignKey(Supplier, related_name='stocks', on_delete=models.CASCADE,null=False,default=1)
    soug = models.ForeignKey(Soug, related_name='stocks', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='stocks', on_delete=models.CASCADE,null=False,default=1)
