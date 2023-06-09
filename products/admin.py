from django.contrib import admin
from .models import Product, Category, ProductStatus
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Displays the Product model in the admin panel
    """
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )
    summernote_fields = "description, features"
    ordering = ("sku",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Displays the Category model in the admin panel
    """
    list_display = (
        "friendly_name",
        "name",
    )

@admin.register(ProductStatus)
class ProductStatusAdmin(admin.ModelAdmin):
    """
    Displays the Product Status model in the admin panel
    """
    list_display = (
        "friendly_name",
        "name",
    )
