from django.contrib import messages
from django.shortcuts import render, redirect

from CHRISTO_USER.forms import UserRegisterForm


def home(request):
    return render(request, "home/home.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Error creating your account. Please check the information provided.')
    else:
        form = UserRegisterForm()
    return render(request, 'home/register.html', {'form': form})
