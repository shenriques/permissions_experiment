from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'organisation')}),
    )
    list_display = ('username', 'email', 'role', 'organisation')

admin.site.register(CustomUser, CustomUserAdmin)