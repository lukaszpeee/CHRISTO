from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def user_home(request):
    return render(request, 'user/user_home.html')


@login_required
def profile(request):
    return render(request, 'user/user_profile.html')

