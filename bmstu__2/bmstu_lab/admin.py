from django.contrib import admin

# Register your models here.
from .models import Company, Views_product

admin.site.register(Company)
admin.site.register(Views_product)