from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from members.models import User


class UserAdmin(BaseUserAdmin):
    pass

admin.site.register(User, UserAdmin)