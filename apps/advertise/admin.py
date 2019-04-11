from django.contrib import admin

from .models import Advertise, AdvertiseImage, Province, County


@admin.register(Advertise)
class AdvertiseModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'expiration_date', 'state')


@admin.register(AdvertiseImage)
class AdvertiseImageModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(County)
admin.site.register(Province)