from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    bio_description = models.CharField(max_length=300)
    password = models.CharField(max_length=100)