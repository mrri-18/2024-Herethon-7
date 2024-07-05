# community/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Accountapp.models import Follow, Member
from Countapp.models import Certification  # Import Certification from Countapp

@login_required
def community_home(request):
    # Get all certifications from other users
    all_certifications = Certification.objects.exclude(user=request.user)

    # Get user profile data
    user = request.user
    followers = Follow.objects.filter(following=user)
    following = Follow.objects.filter(follower=user)

    context = {
        'all_certifications': all_certifications,
        'user': user,
        'followers_count': followers.count(),
        'following_count': following.count(),
    }
    return render(request, 'community/home.html', context)

@login_required
def follower_list(request):
    user = request.user
    followers = Follow.objects.filter(following=user)
    return render(request, 'community/follower_list.html', {'followers': followers})

@login_required
def following_list(request):
    user = request.user
    following = Follow.objects.filter(follower=user)
    return render(request, 'community/following_list.html', {'following': following})
