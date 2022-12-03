from django.contrib import admin

from MiracleArt.admin.pin import PinAdmin
from MiracleArt.admin.pin_category import PinCategoryAdmin
from MiracleArt.models import Pin, PinCategory

admin.site.register(Pin, PinAdmin)
admin.site.register(PinCategory, PinCategoryAdmin)


admin.site.site_header = 'Административная панель'
admin.site.index_title = 'Miracle Art'
