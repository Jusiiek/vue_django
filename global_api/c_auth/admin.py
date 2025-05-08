from django.contrib import admin

from .models import AuthToken


# Register your models here.

class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'user', 'created_at', 'expires_at', 'is_valid')
    search_fields = ('user__email', 'token')
    readonly_fields = ('token', 'created_at')

    def is_valid(self, obj):
        return not obj.is_expired()
    is_valid.boolean = True
    is_valid.short_description = 'Token Valid'

admin.site.register(AuthToken, AuthTokenAdmin)
