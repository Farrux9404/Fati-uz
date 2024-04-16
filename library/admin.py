from django.contrib import admin
from .models import Dissertationabstract, Category, JournalUzbekistan


@admin.register(Dissertationabstract)
class DissertationabstractAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']

@admin.register(JournalUzbekistan)
class JournalUzbekistanAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time']
    list_filter = ['title']
    search_fields = ['title']