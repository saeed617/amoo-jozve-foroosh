from django.db import models
from django.contrib.auth import get_user_model

from apps.advertise.models import Advertise

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    advertises = models.ManyToManyField(Advertise, blank=True)

    def __str__(self):
        return self.user.email + "'s card"
