# profiles/admin.py
from django.contrib import admin
from .models import Profile, Follow, ArchivePost

admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(ArchivePost)
