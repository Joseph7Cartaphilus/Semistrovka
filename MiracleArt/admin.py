from django.contrib import admin

from .models import Pin


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'img', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'text', 'img', 'slug']
    ordering = ['title']
    list_per_page = 10
