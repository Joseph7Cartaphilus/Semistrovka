from django.contrib import admin
from users.admin.user import UserAdmin
from users.models import User

admin.site.register(User, UserAdmin)
