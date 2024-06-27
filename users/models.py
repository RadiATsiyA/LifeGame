from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    """Model of users profile"""
    full_name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    notification_settings = models.JSONField()
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.full_name}"


class UserLevel(models.Model):
    current_level = models.IntegerField(default=1)
    current_exp = models.IntegerField(default=0)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user_id.id} | Level {self.current_level}"


class UserAchievements(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    is_achieved = models.BooleanField(default=False)
    date_achieved = models.DateField(null=True, blank=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.title}"
