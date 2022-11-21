from django.contrib import admin

from .models import Pin, PinCategory


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'category', 'img', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'text', 'category', 'img', 'slug']
    ordering = ['title']
    list_per_page = 10


@admin.register(PinCategory)
class PinCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_per_page = 5
    ordering = ['name']
