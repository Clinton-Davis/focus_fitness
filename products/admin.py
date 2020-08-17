from django.contrib import admin
from .models import Product, Category, productComment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'in_stock', 'display_items', 'category',
                    'price', 'rating', 'image',)

    list_editable = ('in_stock', 'display_items', 'price', 'category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(productComment)
