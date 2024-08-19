from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from homepage_and_profile.forms import ProfileForm
from user_auth.models import User


def home(request):
    return render(request, "homepage_and_profile/homepage.html")


@login_required
def profile(request, user_id, profile_form=None):
    user = get_object_or_404(User, pk=user_id)
    context = {"username": user.username, "user_profile": user.profile}

    if profile_form:
        context["profile_form"] = profile_form

    return render(request, "homepage_and_profile/profile.html", context)


@login_required
def update_profile(request, user_id):
    form = ProfileForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile")

    context = {"form": form}
    return redirect("profile", profile_form=form)
