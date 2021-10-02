
from rest_framework.fields import ReadOnlyField 
from .models import Brandlog, Cashier, Coffre, Credit, Diposite, Expance, Log, Profit, SaleProfit, Withdraw
from rest_framework import serializers



class CashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cashier
        fields = ['sum']
class CashierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cashier
        fields = ['date','amount']
class CoffreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coffre
        fields = ['date','amount']
class WithdrawSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Withdraw
        fields = ['date','amount']
class ProfitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profit
        fields = ['date','amount','brand']
class CreditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credit
        fields = ['date','amount']
class SaleProfitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SaleProfit
        fields = ['date','amount']
class BrandlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brandlog
        fields = ['date','brand']

class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ['name','details','quantity','date','amount']
        

class ExpanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expance
        fields = ['name','details','date','amount']
class DipositeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diposite
        fields = ['name','details','date',"amount",]


