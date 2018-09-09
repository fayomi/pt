from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='profile_image', blank=True)
    location = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username
