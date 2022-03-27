from django.contrib import admin
from .models import (ProductUnit, ProductCategory, Product,
    ProductVariant, ProductPhoto)

class ProductPhotoAdmin(admin.ModelAdmin):
    exclude = ['width', 'height']

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
admin.site.register(ProductUnit)