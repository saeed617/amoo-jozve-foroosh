from django.contrib import admin

from .models import Advertise, AdvertiseImage


@admin.register(Advertise)
class AdvertiseModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'expiration_date', 'state')


@admin.register(AdvertiseImage)
class AdvertiseImageModelAdmin(admin.ModelAdmin):
    pass
