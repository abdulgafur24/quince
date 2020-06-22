from django.contrib import admin
from .models import ProxyUser, ProxyToken
from rest_framework.authtoken.models import Token

admin.site.unregister(Token)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user')


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'is_private', 'is_superuser')
    list_filter = ('groups', 'is_active', 'is_private', 'is_superuser')
    search_fields = ('username', 'biography', 'email', 'first_name', 'last_name')


admin.site.register(ProxyUser, UserAdmin)
admin.site.register(ProxyToken, TokenAdmin)

