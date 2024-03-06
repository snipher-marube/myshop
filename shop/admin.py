from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ('name',)
    }
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    prepopulated_fields = {
        'slug': ('name',)
    }
    list_filter = ['category', 'available', 'created', 'updated']
    date_hierarchy = 'created'
    list_editable = ['price', 'stock', 'available']
    raw_id_fields = ['category']
    search_fields = ['name']
