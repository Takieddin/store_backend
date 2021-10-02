from stock.models import Soug
from sales.serializers import RestoreSerializer
from cashier.serializers import CashSerializer, CashierSerializer, DipositeSerializer, ExpanceSerializer, LogSerializer
from .models import Cashier, Coffre, Credit, Diposite, Expance, Log, Profit, SaleProfit
from django.http.response import HttpResponse, JsonResponse 
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from django.db.models import Sum
from django.db.models.functions import TruncMonth ,TruncDay









        
class CashierViewSet(viewsets.ModelViewSet):
   
    queryset =Cashier.objects.all()
    serializer_class = CashierSerializer
    #permission_classes = [permissions.IsAuthenticated]

class CashAPIView(APIView):
    
    def get(self, request, format=None):
        summery=request.GET.get('s',0)
        content =''
        if summery=='30':
            l=Cashier.objects.annotate(day=TruncDay('date')).values('day').annotate(daily=Sum('amount')).order_by()
            index=min(len(l),30)
            content = {
            'cash_sum': l[len(l)-index:]# `django.contrib.auth.User` instance.
            }
        elif summery=='12':
            content = {
            'cash_sum': Cashier.objects.annotate(month=TruncMonth('date')).values('month').annotate(monthly=Sum('amount')).order_by()# `django.contrib.auth.User` instance.
            }
        else :
            content = {
                'cash_sum': Cashier.objects.aggregate(Sum('amount'))['amount__sum'],  # `django.contrib.auth.User` instance.
            }
        
        return Response(content)

class CoffreAPIView(APIView):
    
    def get(self, request, format=None):
        summery=request.GET.get('s',0)
        content =''
        if summery=='30':
            l=Coffre.objects.annotate(day=TruncDay('date')).values('day').annotate(daily=Sum('amount')).order_by()
            index=min(len(l),30)
            content = {
            'coffre_sum': l[len(l)-index:]# `django.contrib.auth.User` instance.
            }
        elif summery=='12':
            content = {
            'coffre_sum': Coffre.objects.annotate(month=TruncMonth('date')).values('month').annotate(monthly=Sum('amount')).order_by()# `django.contrib.auth.User` instance.
            }
        else :
            content = {
                'coffre_sum': Coffre.objects.aggregate(Sum('amount'))['amount__sum'],  # `django.contrib.auth.User` instance.
            }
        
        return Response(content)
class ProfitAPIView(APIView):
    
    def get(self, request, format=None):
        summery=request.GET.get('s',0)
        content =''
        if summery=='30':
            l=Profit.objects.annotate(day=TruncDay('date')).values('day').annotate(daily=Sum('amount')).order_by()
            index=min(len(l),30)
            content = {
            'profit_sum': l[len(l)-index:]# `django.contrib.auth.User` instance.
            }
        elif summery=='12':
            content = {
            'profit_sum': Profit.objects.annotate(month=TruncMonth('date')).values('month').annotate(monthly=Sum('amount')).order_by()# `django.contrib.auth.User` instance.
            }
        else :
            content = {
                'profit_sum': Profit.objects.aggregate(Sum('amount'))['amount__sum'],  # `django.contrib.auth.User` instance.
            }
        
        return Response(content)
class CreditAPIView(APIView):
    
    def get(self, request, format=None):
        summery=request.GET.get('s',0)
        content =''
        if summery=='30':
            l=Credit.objects.annotate(day=TruncDay('date')).values('day').annotate(daily=Sum('amount')).order_by()
            index=min(len(l),30)
            content = {
            'credit_sum': l[len(l)-index:]# `django.contrib.auth.User` instance.
            }
        elif summery=='12':
            content = {
            'credit_sum': Credit.objects.annotate(month=TruncMonth('date')).values('month').annotate(monthly=Sum('amount')).order_by()# `django.contrib.auth.User` instance.
            }
        else :
            content = {
                'credit_sum': Credit.objects.aggregate(Sum('amount'))['amount__sum'],  # `django.contrib.auth.User` instance.
            }
        
        return Response(content)
class SaleProfitAPIView(APIView):
    
    def get(self, request, format=None):
        summery=request.GET.get('s',0)
        content =''
        if summery=='30':
            l=SaleProfit.objects.annotate(day=TruncDay('date')).values('day').annotate(daily=Sum('amount')).order_by()
            index=min(len(l),30)
            content = {
            'sale_profit_sum': l[len(l)-index:]# `django.contrib.auth.User` instance.
            }
        elif summery=='12':
            content = {
            'sale_profit_sum': SaleProfit.objects.annotate(month=TruncMonth('date')).values('month').annotate(monthly=Sum('amount')).order_by()# `django.contrib.auth.User` instance.
            }
        else :
            content = {
                'sale_profit_sum': SaleProfit.objects.aggregate(Sum('amount'))['amount__sum'],  # `django.contrib.auth.User` instance.
            }
        
        return Response(content)


class DipositeViewSet(viewsets.ModelViewSet):
   
    queryset =Diposite.objects.all()
    serializer_class = DipositeSerializer
    #permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        name=request.data['name']
        details=request.data['details']
        date = datetime.fromtimestamp(
            int(request.data['date'] or 0) / 1000.0) or datetime.now()
        amount=request.data['amount']
        dip=Diposite(name=name,details=details,date=date,amount=amount)
        cash=request.data['cash'] or False
        profit=request.data['profit'] or False
        if cash :
            cashier=Cashier(date=date,amount=+int(amount))
            cashier.save()
        if profit :
            profit=Profit(date=date,amount=+int(amount))
            profit.save()
        dip.save()
        data = DipositeSerializer(dip).data
        return JsonResponse(data=data, status=201)
class LogViewSet(viewsets.ModelViewSet):
   
    queryset =Log.objects.all()
    serializer_class = LogSerializer
    #permission_classes = [permissions.IsAuthenticated]
class ExpanceViewSet(viewsets.ModelViewSet):
   
    queryset =Expance.objects.all()
    serializer_class = ExpanceSerializer
    #permission_classes = [permissions.IsAuthenticated] 
    def create(self, request, *args, **kwargs):
        name=request.data['name']
        details=request.data['details']
        date = datetime.fromtimestamp(
            int(request.data['date'] or 0) / 1000.0) or datetime.now()
        amount=request.data['amount']
        cash=request.data['cash'] or False
        profit=request.data['profit'] or False
       

        exp=Expance(name=name,details=details,date=date,amount=amount)
        cash=request.data['cash'] or False
        profit=request.data['profit'] or False
        if cash :
            cashier=Cashier(date=date,amount=-int(amount))
            cashier.save()
        if profit :
            profit=Profit(date=date,amount=-int(amount))
            profit.save()
        exp.save()
        data = DipositeSerializer(exp).data
        return JsonResponse(data=data, status=201)

