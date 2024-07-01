
from django.db import models

class Record(models.Model):
    msec=models.IntegerField(default=0) #총 걸은 시간
    distance = models.FloatField() #총 걸은 거리
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.distance} km"
