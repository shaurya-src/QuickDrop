from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    desc = models.CharField(max_length=140,blank=True)
    avatar = models.ImageField(upload_to='avatars/',default='avatars/default.png')