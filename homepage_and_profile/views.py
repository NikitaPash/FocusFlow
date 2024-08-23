from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from copy import deepcopy

from homepage_and_profile.forms import ProfileForm, EditUsernameForm
from user_auth.models import User


def home(request):
    return render(request, "homepage_and_profile/homepage.html")


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_copy = deepcopy(user)

    if request.method == "POST":
        if request.user == user:
            profile_form = ProfileForm(request.POST, request.FILES, instance=user_copy.profile)
            username_form = EditUsernameForm(request.POST, instance=user_copy)
            if profile_form.is_valid() and username_form.is_valid():
                profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
                username_form = EditUsernameForm(request.POST, instance=user)
                profile_form.save()
                username_form.save()
                return redirect("profile", user.username)
        else:
            raise PermissionDenied()
    else:
        profile_form = ProfileForm(instance=user.profile)
        username_form = EditUsernameForm(instance=user)

    link_fields = [
        {"name": "Website", "icon": "fas fa-globe", "link": f"{user.profile.website}", },
        {"name": "GitHub", "icon": "fab fa-github", "link": f"{user.profile.github}"},
        {"name": "LinkedIn", "icon": "fa-brands fa-linkedin-in", "link": f"{user.profile.linkedin}"},
        {"name": "Email", "icon": "fa-solid fa-envelope", "link": f"mailto:{user.profile.email}"}
    ]

    link_fields = [item for item in link_fields if item["link"]]

    user = get_object_or_404(User, username=username)
    context = {
        "link_fields": link_fields,
        "user": user,
        "profile_form": profile_form,
        "username_form": username_form,
    }
    return render(request, "homepage_and_profile/profile.html", context)
