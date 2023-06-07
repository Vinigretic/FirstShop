from django.contrib import admin
from .models import *
from import_export import fields, resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Product


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin, TranslationAdmin):
    resource_class = ProductResource
    list_display = ['id', 'name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}









