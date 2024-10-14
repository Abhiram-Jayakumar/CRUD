from django.db import models

from User.models import UserProfile

# Create your models here.
class Vlog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() 
    published_date = models.DateTimeField(auto_now_add=True) 
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  