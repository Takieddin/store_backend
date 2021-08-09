from cashier.models import Cashier, Diposite,Log,Expance,Restore
from django.http.response import HttpResponse, JsonResponse 
from django.shortcuts import render
from django.views.generic.base import View
from models import Cashier

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




        
class CashierViewSet(viewsets.ModelViewSet):
   
    queryset =Cashier.objects.all()
    serializer_class = CashierSerializer
    #permission_classes = [permissions.IsAuthenticated]
class DipositeViewSet(viewsets.ModelViewSet):
   
    queryset =Diposite.objects.all()
    serializer_class = DipositeSerializer
    #permission_classes = [permissions.IsAuthenticated]
class LogViewSet(viewsets.ModelViewSet):
   
    queryset =Log.objects.all()
    serializer_class = LogSerializer
    #permission_classes = [permissions.IsAuthenticated]
class ExpanceViewSet(viewsets.ModelViewSet):
   
    queryset =Expance.objects.all()
    serializer_class = ExpanceSerializer
    #permission_classes = [permissions.IsAuthenticated] 
class RestoreViewSet(viewsets.ModelViewSet):
   
    queryset =Restore.objects.all()
    serializer_class = RestoreSerializer
    #permission_classes = [permissions.IsAuthenticated] 
"""    
class CategoryViewSet(viewsets.ModelViewSet):
   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    '''def get_queryset(self):
        user = self.request.user
        b=Budget.objects.filter(user=user)
        return Category.objects.filter(budget=b[0])'''
    def create(self, request, *args, **kwargs):
        b=Budget.objects.get(pk=request.data['budget_id'])
        c=Category(budget=b,**request.data)
        c.save()
        data = CategorySerializer(c).data

        return JsonResponse(data=data, status=201)
    permission_classes = [permissions.AllowAny]
class RowViewSet(viewsets.ModelViewSet):
   
    queryset = Row.objects.all()
    serializer_class = RowSerializer
    '''def get_queryset(self):
        user = self.request.user
        b=Budget.objects.filter(user=user)
        c=Category.objects.filter(budget=b[0])
        return Row.objects.filter(category=c[0])'''
    def create(self, request, *args, **kwargs):
        b=Budget.objects.get(pk=request.data['budget_id'])
        print("b=")
        print(b)
        c=b.categories.get(pk=request.data['category_id'])
        print("c=")
        print(c)
        r=Row(category=c,text=request.data["text"],value=0)
        print("r=")
        print(r)
        r.save()
        print("ee")
        data = RowSerializer(r).data
        return JsonResponse(data=data, status=201)
    permission_classes = [permissions.AllowAny]"""