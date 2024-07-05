
from django.db import models

from Accountapp.models import Member


class Record(models.Model):
    user=models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    msec=models.IntegerField(default=0) #총 걸은 시간
    distance = models.FloatField(default=0) #총 걸은 거리
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.distance} km"

class Certification(models.Model):
    walk_image = models.ImageField(upload_to='certifications/')
    archive_image = models.ImageField(upload_to='archives/',blank=True, null=True)
    description = models.TextField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"Image by {self.user.username} on {self.create_at}"