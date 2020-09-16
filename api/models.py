from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Messages(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_room = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} - {self.chat_room} - {self.timestamp}"
