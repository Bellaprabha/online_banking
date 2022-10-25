from django.contrib import admin
from accounts.models import Customers

# Register your models here.
@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display=('customerid','name','Account_no','Branch','IFSC','phone','Address')
    
    
    # admin.site.register(Customers)