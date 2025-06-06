from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from apps.account.models.profile_model import Profile


User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):

    if created:
        Profile.objects.create(user=instance)
