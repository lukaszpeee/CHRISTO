from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from CHRISTO_USER.forms import UserUpdateForm, ProfileUpdateForm


@login_required
def user_home(request):
    return render(request, 'user/user_home.html')


@login_required
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user/user_profile.html', context)


@login_required
def user_twitter_profiles_lists(request):
    return render(request, 'user/user_twitter_profiles_lists.html')


@login_required
def user_twitter_profiles_list(request):
    return render(request, 'user/user_twitter_profiles_list_details.html')

