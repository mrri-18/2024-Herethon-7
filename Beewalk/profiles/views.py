from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MemberUpdateForm


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = MemberUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('homeapp:home')
    else:
        form = MemberUpdateForm(instance=request.user)

    return render(request, 'profiles/edit_profile.html', {'form': form})
