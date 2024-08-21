from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from homepage_and_profile.forms import ProfileForm
from user_auth.models import User


def home(request):
    return render(request, "homepage_and_profile/homepage.html")


@login_required
def profile(request, username):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("profile", username)
    else:
        profile_form = ProfileForm(instance=request.user.profile)

    user = get_object_or_404(User, username=username)
    context = {
        "username": username,
        "user_profile": user.profile,
        "profile_form": profile_form,
    }
    return render(request, "homepage_and_profile/profile.html", context)
