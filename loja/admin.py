from django.contrib import admin
from .models import Category, Product, Size, Marca, ProductAttribute

# Register your models here.

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Marca)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'marca', 'size', 'status')
    list_editable = ('status',)
admin.site.register(Product, ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'size')

admin.site.register(ProductAttribute, ProductAttributeAdmin)
