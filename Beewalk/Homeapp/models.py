from django.db import models

# Create your models here.

from django.db import models

class ExerciseInfo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='exercise_images/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models

class WalkingCourse(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='walking_course_images/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
