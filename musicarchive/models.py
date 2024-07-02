from django.db import models
from django.conf import settings
from Accountapp.models import Member
from django.utils import timezone

class MusicArchive(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='musicarchive/images/', default=None)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
