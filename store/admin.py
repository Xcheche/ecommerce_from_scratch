from django.contrib import admin
from store.models import Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "original_price", "selling_price", "quantity", "status")
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "status")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)