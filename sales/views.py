from copy import error
from stock.models import Stock
from cashier.models import Cashier, Profit, SaleProfit
from sales.models import Payment,Basket,Restore,Client, Process
from sales.serializers import  BasketSerializer, ClientSerializer, PaymentSerializer, ProcessSerializer, RestoreSerializer
from django.http.response import HttpResponse, JsonResponse 
from django.shortcuts import render
from django.views.generic.base import View
from datetime import datetime


# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import authenticate


from rest_framework.authentication import  BasicAuthentication #SessionAuthentication,
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Auth(APIView):
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
        }
        return Response(content)
class ClientViewSet(viewsets.ModelViewSet):
   
    queryset =Client.objects.all()
    serializer_class = ClientSerializer
    #permission_classes = [permissions.IsAuthenticated]
class ProcessViewSet(viewsets.ModelViewSet):
   
    queryset =Process.objects.all()
    serializer_class = ProcessSerializer
    #permission_class es = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        client=Client.objects.get(id=request.data['client_id'])
        date = datetime.fromtimestamp(
            int(request.data['date'] or 0) / 1000.0) or datetime.now()
        paied=request.data['paied']or 0
        total=request.data['total'] or 0
        i=1
        p=Process(client=client,date=date,total=total,name=request.data['name'] or 'process',paied=paied)
        p.save()
        cashier=Cashier(date=date,amount=+int(paied))
        sufficient =True
        faida=0

        for basket in request.data['baskets']:
            stock=Stock.objects.get(id=basket["id"])
            name = "basket "+str(i)
            i+=1
            quantity=basket["quantity"]
            prix_final=basket["prix_final"]
            if quantity<=stock.instock:
                faida=faida+int(prix_final)-int(stock.item_buying_price)
                stock.instock -=quantity
                stock.save()
                b=Basket(name=name,quantity=quantity,date=date,prix_final=prix_final,process=p,stock=stock)
                b.save()
            else:
                sufficient=False
                break
        
        profit=Profit(date=date,amount=+int(faida))
        sprofit=SaleProfit(date=date,amount=+int(faida))
        if sufficient:
            cashier.save()
            sprofit.save()
            profit.save()
            pa=Payment(client=client,date=date,amount=paied,process=p)
            pa.save()
            data = ProcessSerializer(p).data
            return JsonResponse(data=data, status=201)
        else:
            p.delete()
            return JsonResponse(data={"error":'insufficiant stock'}, status=409)
class PaymentViewSet(viewsets.ModelViewSet):
   
    queryset =Payment.objects.all()
    serializer_class = PaymentSerializer
    #permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        client=Client.objects.get(id=request.data['client_id'])
        process=Process.objects.get(id=request.data['process_id'])
        date = datetime.fromtimestamp(
            int(request.data['date'] or 0) /1000.0) or datetime.now()
        amount=request.data['amount'] or 0
        process.paied+=amount
        process.save()
        cashier=Cashier(date=date,amount=+int(amount))
        cashier.save()

        p=Payment(client=client,date=date,amount=amount,process=process)
        p.save()
        data = PaymentSerializer(p).data
        return JsonResponse(data=data, status=201)
class BasketViewSet(viewsets.ModelViewSet):
   
    queryset =Basket.objects.all()
    serializer_class = BasketSerializer
    #permission_classes = [permissions.IsAuthenticated] 
class RestoreViewSet(viewsets.ModelViewSet):

    queryset =Restore.objects.all()
    serializer_class = RestoreSerializer
    def create(self, request, *args, **kwargs):
        client=Client.objects.get(id=request.data['client_id'])
        basket=Basket.objects.get(id=request.data['basket_id'])
        date = datetime.fromtimestamp(
            int(request.data['date'] or 0) / 1000.0) or datetime.now()
        total=request.data['total'] 
        quantity=request.data['quantity']
        cashier=Cashier(date=date,amount=-int(total))
        cashier.save()
        profit=Profit(date=date,amount=-int(total))
        profit.save()
        sprofit=SaleProfit(date=date,amount=-int(total))
        sprofit.save()
        stock=Stock.objects.get(id=basket.stock.id)
        stock.quantity+=quantity
        stock.save()
        r=Restore(client=client,basket=basket,date=date,total=total,quantity=quantity)
        r.save()
        data = RestoreSerializer(r ).data
        return JsonResponse(data=data, status=201)
   
    #permission_classes = [permissions.IsAuthenticated] 