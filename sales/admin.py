from django.contrib import admin


from .models import Client,Basket,Process,Payment,Restore

admin.site.register(Client)
admin.site.register(Basket)
admin.site.register(Process)
admin.site.register(Payment)
admin.site.register(Restore)
