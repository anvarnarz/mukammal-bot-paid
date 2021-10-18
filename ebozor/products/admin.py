from django.contrib import admin

# Register your models here.
from .models import User, Product

admin.site.register(User)
admin.site.register(Product)