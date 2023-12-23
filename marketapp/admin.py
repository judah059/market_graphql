from django.contrib import admin

from marketapp.forms import ProductAdminForm
from marketapp.models import Shop, Product, ShopType, ProductCategory


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    class Media:
        js = ['admin.js']
    # pass


@admin.register(ShopType)
class ShopTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass
