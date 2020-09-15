from django.contrib import admin
from .models import Product, Category, productComment, ProductView


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'in_stock', 'sales_items',
                    'was_price', 'price', 'category',
                    'rating_ave', 'view_count',)

    list_editable = ('in_stock', 'sales_items',
                     'was_price', 'price', 'category',)

    list_filter = ('category', 'in_stock',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product',)


admin.site.register(ProductView, ProductViewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(productComment)
