from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    """Model of users profile"""
    full_name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    notification_settings = models.JSONField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.full_name}"


class Goal(models.Model):
    """Model for users main goals"""
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=3000, null=True, blank=True)
    category = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    is_done = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.title}"


class Task(models.Model):
    """Tasks for user to achieve main goal"""
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=3000)
    created_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    is_done = models.BooleanField(default=False)
    goal_id = models.ForeignKey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.is_done}"


class Subtask(models.Model):
    """Subtasks of task"""
    title = models.CharField(max_length=300)
    desctiprion = models.TextField(max_length=3000)
    created_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    is_done = models.BooleanField(default=False)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | {self.is_done}"


class UserLevel(models.Model):
    current_level = models.IntegerField(default=1)
    current_exp = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user.id} | Level {self.current_level}"


class UserAchievements(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    is_achieved = models.BooleanField(default=False)
    date_achieved = models.DateField(null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.title}"


class Friendship(models.Model):
    STATUS = [
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected")
    ]

    status = models.CharField(max_length=30, choices=STATUS, default="Pending")
    user = models.ForeignKey(User, related_name='friendships', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'friend')

    def __str__(self):
        return f"{self.user.username} - {self.friend.username} ({self.status})"





