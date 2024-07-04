# profiles/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Follow, ArchivePost

def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    posts = ArchivePost.objects.filter(user=user)
    followers = Follow.objects.filter(followed=user).count()
    following = Follow.objects.filter(follower=user).count()
    return render(request, 'profiles/profile.html', {
        'user': user,
        'profile': profile,
        'posts': posts,
        'followers': followers,
        'following': following
    })

def feed(request):
    posts = ArchivePost.objects.all().order_by('-created')
    return render(request, 'profiles/feed.html', {'posts': posts})
