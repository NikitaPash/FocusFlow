from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import auth

from .forms import CreateUserForm, LoginForm
from .decorators import user_not_authenticated


@user_not_authenticated
def register_view(request):
    form = CreateUserForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('login')

    context = {'registerform': form}

    return render(request, 'user_auth/register.html', context)


@user_not_authenticated
def login_view(request):
    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

    context = {'loginform': form}

    return render(request, 'user_auth/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
