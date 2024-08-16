from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetConfirmView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import auth
from django.urls import reverse_lazy

from .forms import CreateUserForm, LoginForm, MyPasswordResetForm, MySetPasswordForm
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
    reset_form = MyPasswordResetForm(request.POST or None)

    if request.method == 'POST':
        print(form.errors)
        if 'login_submit' in request.POST and form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                auth.login(request, user)
                if remember_me:
                    request.session.set_expiry(604800)
                else:
                    request.session.set_expiry(0)
                return redirect('home')

        elif 'reset_submit' in request.POST and reset_form.is_valid():
            reset_form.save(request=request,
                            html_email_template_name='user_auth/forgot_password/password_reset_email.html',
                            subject_template_name='emails/password_reset_subject.txt',
                            email_template_name='emails/password_reset_email.txt', )
            return redirect('password_reset_done')

    context = {'loginform': form, 'reset_form': reset_form}
    return render(request, 'user_auth/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = MySetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'user_auth/forgot_password/password_reset_confirm.html'
