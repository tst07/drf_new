from django.contrib import admin
from .models import Bank, Branch, Accounts, Customer, BanksInfo

# Register your models here.

class BanksInfoInline(admin.TabularInline):
	model = BanksInfo
	extra = 2

class CustomerAdmin(admin.ModelAdmin):
	inlines = (BanksInfoInline,)


admin.site.register(Bank)
admin.site.register(Accounts)
admin.site.register(Branch)
admin.site.register(Customer, CustomerAdmin)
