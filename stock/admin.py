from django.contrib import admin

# Register your models here.
from .models import Category,Brand,Supplier,Soug,Stock,Clearance
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Supplier)
admin.site.register(Soug)
admin.site.register(Stock)
admin.site.register(Clearance)
