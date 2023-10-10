from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = ((CREATOR, 'Creator'), (SUBSCRIBER, 'Subscriber'),)

    profile_picture = models.ImageField(verbose_name='Profil picture')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="Role")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.role == self.CREATOR:
            group = Group.objects.get(name='creators')
            group.user_set.add(self)
        elif self.role == self.SUBSCRIBER:
            group = Group.objects.get(name='subscribers')
            group.user_set.add(self)
