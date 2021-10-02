from stock.serializers import BrandSerializer, CategorySerializer, ClearanceSerializer, SougSerializer, StockSerializer, SupplierSerializer
from stock.models import Category, Clearance, Supplier
from cashier.models import Cashier, Diposite, Profit, Stock, Soug, Brand
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from datetime import datetime


# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import authenticate


from rest_framework.authentication import BasicAuthentication  # SessionAuthentication,
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Auth(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
        }
        return Response(content)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAuthenticated]


class SupplierViewSet(viewsets.ModelViewSet):

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    #permission_classes = [permissions.IsAuthenticated]


class StockViewSet(viewsets.ModelViewSet):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        context = {'request': request}
        brand = Brand.objects.get(id=request.data['brand_id'])
        # soug=Soug.objects.get(id=request.data['soug_id'])
        supplier = Supplier.objects.get(id=request.data['supplier'])
        name = request.data['name']
        note = request.data['note'] or ' '
        quantity = int(request.data['quantity'])
        date = datetime.fromtimestamp(
            int(request.data['date'] or 0) / 1000.0) or datetime.now()
        item_buying_price = int(request.data['item_buying_price'])
        item_sale_price = int(request.data['item_sale_price'])
        subprofit = int(request.data['subprofit']) or False
        subcash = int(request.data['subcash']) or False
        clearance = int(request.data['clearance'] or quantity*item_buying_price)

        if subcash :
            cashier=Cashier(date=date,amount=-int(clearance))
            cashier.save()
        if subprofit :
            profit=Profit(date=date,amount=-int(clearance))
            profit.save()

        stock = Stock(brand=brand, supplier=supplier, name=name, note=note, quantity=quantity,instock=quantity,
                      date=date, item_buying_price=item_buying_price, item_sale_price=item_sale_price)
        stock.save()
        c=Clearance(date=date,stock=stock,supplier=supplier,amount=int(clearance))
        c.save()
        data = StockSerializer(stock ,context=context).data
        return JsonResponse(data=data, status=201)


class SougViewSet(viewsets.ModelViewSet):

    queryset = Soug.objects.all()
    serializer_class = SougSerializer


class ClearanceViewSet(viewsets.ModelViewSet):

    queryset = Clearance.objects.all()
    serializer_class = ClearanceSerializer
    #permission_classes = [permissions.IsAuthenticated]


class BrandViewSet(viewsets.ModelViewSet):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def create(self, request, *args, **kwargs):
        context = {'request': request}
        c = Category.objects.get(id=request.data['category_id'])
        b = Brand(category=c, name=request.data["name"])
        b.save()
        data = BrandSerializer(b).data
        return JsonResponse(data=data, status=201)
    #permission_classes = [permissions.IsAuthenticated]
