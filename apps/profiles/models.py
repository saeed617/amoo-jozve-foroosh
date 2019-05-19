from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.translation import ugettext_lazy as _
from apps.utils.uuname import unique_username_generator

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # extra fields

    def __str__(self):
        return self.user.email


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.username:
        instance.username = unique_username_generator(instance)


def post_save_receiver(sender, instance,created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)


pre_save.connect(pre_save_receiver, sender=User)
post_save.connect(post_save_receiver, sender=User)
