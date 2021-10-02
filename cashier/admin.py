from django.contrib import admin

# Register your models here.
from .models import Cashier,Log,Expance,Diposite, Profit
admin.site.register(Cashier)
admin.site.register(Log)
admin.site.register(Expance)
admin.site.register(Diposite)
admin.site.register(Profit)
