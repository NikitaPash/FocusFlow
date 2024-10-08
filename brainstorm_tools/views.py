from allauth.core.internal.httpkit import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.cache import cache_page

from user_auth.models import User
from .forms import ProjectForm
from .models import Feature, SubFeature, Project


@login_required
def create_project(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)

        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user
            project.save()

            features = project_form.cleaned_data.get("features", [])
            feature_counter = 0

            for feature_name in features:
                feature = Feature.objects.create(
                    project=project, feature_name=feature_name
                )

                subfeatures_key = f"subfeature_name_{feature_counter}_"
                subfeatures = [
                    value
                    for key, value in request.POST.items()
                    if key.startswith(subfeatures_key)
                ]

                for subfeature_name in subfeatures:
                    if subfeature_name.strip():
                        SubFeature.objects.create(
                            feature=feature, subfeature_name=subfeature_name
                        )

                feature_counter += 1

            return redirect(reverse("view_projects", args=[request.user.username]))
    else:
        project_form = ProjectForm()

    creation_form_context = {
        "project_form": project_form,
    }

    return render(
        request, "brainstorm_tools/create_project.html", context=creation_form_context
    )


@login_required
def view_projects(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        search_query = request.POST.get('search_query', '').strip()
        if search_query:
            projects = Project.objects.filter(user=user, title__icontains=search_query).order_by('-pub_date')
        else:
            projects = Project.objects.filter(user=user).order_by('-pub_date')
    else:
        projects = Project.objects.filter(user=user).order_by('-pub_date')

    page = request.GET.get('page', 1)
    items_per_page = 5
    paginator = Paginator(projects, items_per_page)

    try:
        projects_page = paginator.page(page)
    except PageNotAnInteger:
        projects_page = paginator.page(1)
    except EmptyPage:
        projects_page = paginator.page(paginator.num_pages)

    project_view_context = {
        "projects_page": projects_page,
        "username": username,
    }
    return render(
        request, "brainstorm_tools/projects.html", context=project_view_context
    )
