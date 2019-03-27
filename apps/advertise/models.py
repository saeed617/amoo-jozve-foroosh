from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Advertise(models.Model):
    PUBLIC = 'P'
    MAJOR_CHOICES = (
        (PUBLIC, _('Public')),
        ('CE', _('Computer Engineering')),
        ('EE', _('Electrical Engineering')),
    )

    PENDING = 'P'
    PUBLISHED = 'PB'
    CLOSED = 'C'
    STATE_CHOICES = (
        (PENDING, _('Pending')),
        (PUBLISHED, _('Published')),
        (CLOSED, _('Closed')),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(max_length=2000, verbose_name=_('Description'))
    expiration_date = models.DateTimeField(blank=True, null=True,
                                           verbose_name=_('Expiration date'))  # null = never expire
    price = models.PositiveIntegerField(verbose_name=_('Price'))
    major = models.CharField(max_length=10, choices=MAJOR_CHOICES, default=PUBLIC, verbose_name=_('Major'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=PENDING, verbose_name=_('State'))
    page_numbers = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Page numbers'))
    publisher = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Publisher'))
    release_year = models.CharField(max_length=4, null=True, blank=True, verbose_name=_('Release year'))

    # TODO: images, city

    def __str__(self):
        return self.title


class AdvertiseImage(models.Model):
    ADVERTISE_IMAGE_UPLOAD_PATH = 'advertise/images'
    advertise = models.ForeignKey(Advertise, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=ADVERTISE_IMAGE_UPLOAD_PATH, verbose_name=_('Advertise image'))

    def __str__(self):
        return self.advertise.title
