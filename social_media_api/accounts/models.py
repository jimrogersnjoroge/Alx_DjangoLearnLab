from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
#Creating Custom User Model
class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    followers = models.ManyToManyField('self', related_name='user_following', symmetrical=False, blank=True)
    following = models.ManyToManyField('self', related_name='user_followers', symmetrical=False, blank=True)

    def __str__(self):
        return self.username

