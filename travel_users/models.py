from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='photos/%Y', blank=True)
    phone = PhoneNumberField(blank=True)
    emergency_first_name = models.CharField(max_length=255, blank=True)
    emergency_last_name = models.CharField(max_length=255, blank=True)
    emergency_phone = PhoneNumberField()
    emergency_email = models.EmailField(max_length=255, blank=False)
    allergies = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def get_profile(self):
        user = self.objects.all()
        return user

    def __str__(self):
        return self.first_name

