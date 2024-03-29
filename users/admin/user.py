from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'image']
    filter_horizontal = ['groups', 'user_permissions']
    fields = ['password', 'last_login', 'groups', ('username', 'email'), ('first_name', 'last_name'), 'image',
              ('is_active', 'is_staff')]
    ordering = ['-is_staff']
