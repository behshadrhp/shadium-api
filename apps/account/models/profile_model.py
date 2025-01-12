from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _ 

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from utils.type.account.gender_type import GenderType
from apps.account.models.time_stamped_model import TimeStamped


User = get_user_model()

class Profile(TimeStamped):

    # relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    followers = models.ManyToManyField("self", symmetrical=False, related_name="user_followers", blank=True)

    # initial information
    avatar = models.ImageField(verbose_name=_("Avatar"), default="default/avatar.png", upload_to="profile/avatar/")
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, null=True, blank=True)
    biography = models.TextField(verbose_name=_("Biography"), null=True, blank=True)
    gender = models.CharField(verbose_name=_("Gender"), choices=GenderType.choices, max_length=10, null=True, blank=True)
    country = CountryField(verbose_name=_("Country"), null=True, blank=True)
    city = models.CharField(verbose_name=_("City"), max_length=50, null=True, blank=True)
    twitter = models.CharField(verbose_name=_("Twitter"), max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.user.email}"
    
    def follow(self, profile):
        self.followers.add(profile)

    def unfollow(self, profile):
        self.followers.remove(profile)

    def check_following(self, profile):
        return self.followers.filter(pkid=profile.pkid).exists()
