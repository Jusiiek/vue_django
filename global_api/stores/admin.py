from django.contrib import admin
from django.utils.timesince import timesince
from django.utils.timezone import now

from .models import Store


# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ('domain', 'user', 'created_at', 'expires_at', 'created')
    search_fields = ('user__email', 'domain')

    def created(self, obj):
        return f"{timesince(obj.date_joined, now())} ago"

admin.site.register(Store, StoreAdmin)
