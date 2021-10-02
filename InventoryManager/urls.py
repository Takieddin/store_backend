from cashier.views import CashAPIView,  CoffreAPIView,  CreditAPIView,  ProfitAPIView,  SaleProfitAPIView
from cashier.views import  CashierViewSet, DipositeViewSet, ExpanceViewSet
from stock.views import BrandViewSet, CategoryViewSet, ClearanceViewSet, SougViewSet, StockViewSet, SupplierViewSet
from stock.serializers import CategorySerializer
from django.conf.urls import include
from django.contrib import admin
from django.urls import path ,include
from rest_framework import routers
from sales.views import BasketViewSet ,ClientViewSet ,PaymentViewSet ,ProcessViewSet, RestoreViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'cashier', CashierViewSet)
router.register(r'diposites', DipositeViewSet)
router.register(r'supliers', SupplierViewSet)
router.register(r'processes', ProcessViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'sougs', SougViewSet)
router.register(r'cashs', CashierViewSet)
router.register(r'expances', ExpanceViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'restores', RestoreViewSet)
router.register(r'clearances', ClearanceViewSet)








# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cash/', CashAPIView.as_view()),
    path('coffre/', CoffreAPIView.as_view()),
    path('profit/', ProfitAPIView.as_view()),
    path('favicon.ico/', ProfitAPIView.as_view()),
    path('', ProfitAPIView.as_view()),
    path('credit/', CreditAPIView.as_view()),
    path('saleprofit/', SaleProfitAPIView.as_view()),
    path('admin/', admin.site.urls),

]


