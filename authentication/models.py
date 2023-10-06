from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = ((CREATOR, 'Creator'), (SUBSCRIBER, 'Subscriber'),)

    profile_picture = models.ImageField(verbose_name='Profil picture')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="Role")
