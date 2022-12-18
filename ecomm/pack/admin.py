from django.contrib import admin

# Register your models here.
from pack.models import Category
admin.site.register(Category)
from pack.models import Product
admin.site.register(Product)
from pack.models import Cart
admin.site.register(Cart)
from pack.models import Products
from pack.models import Advatisment
from pack.models import Customer
# Register your models here.
from .models import Products
admin.site.register(Products)
from .models import Advatisment
admin.site.register(Advatisment)
from .models import Customer
admin.site.register(Customer)
from .models import Orders
admin.site.register(Orders)