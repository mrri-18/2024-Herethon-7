# community/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Archive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='community/archives/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Archive by {self.user.username} at {self.created_at}"
