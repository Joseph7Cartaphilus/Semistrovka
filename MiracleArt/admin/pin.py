from import_export import resources
from import_export.admin import ImportExportModelAdmin

from MiracleArt.models import Pin


class PinResource(resources.ModelResource):
    class Meta:
        model = Pin
        fields = ('title', 'text', 'category__name', 'img', 'slug', 'user__username')
        export_order = ('title', 'text', 'category__name', 'img', 'slug', 'user__username')


class PinAdmin(ImportExportModelAdmin):
    fields = ['title', 'text', 'category', 'user', 'img', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'text', 'category', 'user', 'img', 'slug']
    ordering = ['title']
    list_per_page = 20
    resource_classes = [PinResource]
