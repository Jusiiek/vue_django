from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.timesince import timesince
from django.utils.timezone import now

from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        'email',
        'is_global_user',
        'is_active',
        'is_superuser',
        'is_staff',
        'created'
    )

    readonly_fields = ('date_joined',)

    def created(self, obj):
        return f"{timesince(obj.date_joined, now())} ago"

    created.short_description = 'Created'


admin.site.register(User, CustomUserAdmin)
