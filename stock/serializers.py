from cashier.serializers import ExpanceSerializer
from django.contrib.auth.models import User, Group
from .models import  Category, Brand, Clearance, Soug, Stock, Supplier
from rest_framework import serializers




class StockSerializer(serializers.HyperlinkedModelSerializer):
    brand_name = serializers.CharField(read_only=True, source="brand.name")

    class Meta:
        model = Stock
        fields = ['id','name','note','quantity','date','item_buying_price','item_sale_price','instock','supplier_id','clearances','brand_id','brand_name']
class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','name','category_id']
        depth =1
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        depth = 2
class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    paied = serializers.IntegerField(read_only=True)
    total = serializers.IntegerField(read_only=True)
    delais = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Supplier
        fields = ['id','name','phone','total','paied','delais']
class SougSerializer(serializers.HyperlinkedModelSerializer):
    stocks=StockSerializer(many=True, read_only=True)
    expances=ExpanceSerializer(many=True, read_only=True)
    class Meta:
        model = Soug
        fields = ['id','name','note','date','total','paied','expances','stocks']
class ClearanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clearance
        fields = ['id','date','amount','supplier_id','stock_id']


