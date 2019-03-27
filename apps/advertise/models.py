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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    expiration_date = models.DateTimeField(blank=True, null=True)  # null = never expire
    price = models.PositiveIntegerField()
    major = models.CharField(max_length=10, choices=MAJOR_CHOICES, default=PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=PENDING)
    page_numbers = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    release_year = models.CharField(max_length=4, null=True, blank=True)

    # TODO: images, city

    def __str__(self):
        return self.title
