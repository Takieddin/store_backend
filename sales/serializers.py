from .models import Basket, Client, Payment, Process, Restore

from rest_framework import serializers



class ClientSerializer(serializers.HyperlinkedModelSerializer):
    paied = serializers.IntegerField(read_only=True)
    total = serializers.IntegerField(read_only=True)
    delais = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Client
        fields = ['id','name','phone','paied','total','delais']
class BasketSerializer(serializers.HyperlinkedModelSerializer):
    stock_name = serializers.CharField(read_only=True, source="stock.name")
    brand_name = serializers.CharField(read_only=True, source="stock.brand.name")
    class Meta:
        model = Basket
        fields = ['id','name','quantity','date',"prix_final","process_id","stock_id","stock_name","brand_name"]
        

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    process_total = serializers.CharField(read_only=True, source="process.total")
    class Meta:
        model = Payment
        fields = ['id','client_id','amount','date','process_id','process_total']

class ProcessSerializer(serializers.HyperlinkedModelSerializer):
    baskets=BasketSerializer(many=True)
    payments=PaymentSerializer(many=True)
    class Meta:
        model = Process
        fields = ['id','name','client_id','total','date','paied', 'payments','baskets']
class RestoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restore
        fields = ['id','client_id','total','quantity',"date","basket_id"]


