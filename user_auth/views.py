from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def register_view(request):
    return render(request, 'user_auth/register.html')


def login_view(request):
    return render(request, 'user_auth/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
