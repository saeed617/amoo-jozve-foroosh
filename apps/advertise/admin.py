from django.contrib import admin

from .models import Advertise


@admin.register(Advertise)
class AdvertiseModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'expiration_date', 'state')
    readonly_fields = ('user',)
