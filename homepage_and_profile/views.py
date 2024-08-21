from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied

from homepage_and_profile.forms import ProfileForm
from user_auth.models import User


def home(request):
    return render(request, "homepage_and_profile/homepage.html")


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        if request.user != user:
            raise PermissionDenied()
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("profile", username)
    else:
        profile_form = ProfileForm(instance=request.user.profile)

    link_fields = [
        {"name": "Website", "icon": "fas fa-globe", "link": f"{user.profile.website}", },
        {"name": "GitHub", "icon": "fab fa-github", "link": f"{user.profile.github}"},
        {"name": "LinkedIn", "icon": "fa-brands fa-linkedin-in", "link": f"{user.profile.linkedin}"},
        {"name": "Email", "icon": "fa-solid fa-envelope", "link": f"mailto:{user.profile.email}"}
    ]

    link_fields = [item for item in link_fields if item["link"]]

    context = {
        "link_fields": link_fields,
        "user": user,
        "profile_form": profile_form,
    }
    return render(request, "homepage_and_profile/profile.html", context)
