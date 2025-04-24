# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# ✅ ইউজার মডেল কাস্টমাইজ করে অ্যাডমিনে রেজিস্টার করছি
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('পারসোনাল ইনফো', {'fields': ('name',)}),
        ('পারমিশন', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
