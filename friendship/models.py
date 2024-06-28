from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#
# class Friendship(models.Model):
#     STATUS = [
#         ("Pending", "Pending"),
#         ("Accepted", "Accepted"),
#         ("Rejected", "Rejected")
#     ]
#
#     status = models.CharField(max_length=30, choices=STATUS, default="Pending")
#     user = models.ForeignKey(CustomUser, related_name='friendships', on_delete=models.CASCADE)
#     friend = models.ForeignKey(CustomUser, related_name='friends', on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('user', 'friend')
#
#     def __str__(self):
#         return f"{self.user.username} - {self.friend.username} ({self.status})"
