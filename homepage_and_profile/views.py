from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from user_auth.models import User


def home(request):
    return render(request, 'homepage_and_profile/homepage.html')


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user_profile': user}
    return render(request, 'homepage_and_profile/profile.html', context)
