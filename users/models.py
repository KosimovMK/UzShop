from django.db import models

from django.contrib.auth.models import AbstractUser

from django import forms

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
