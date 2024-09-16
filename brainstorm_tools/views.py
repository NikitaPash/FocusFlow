from lib2to3.fixes.fix_input import context

from allauth.core.internal.httpkit import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

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

            return redirect("create_project")
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
    projects = Project.objects.filter(user=user).order_by('-pub_date')
    projects_list = []
    features_list = []
    subfeatures_list = []

    for project in projects:
        projects_list.append(project)
        features = Feature.objects.filter(project=project)
        if features.exists():
            for feature in features:
                features_list.append(feature)
                subfeatures = SubFeature.objects.filter(feature=feature)
                if subfeatures.exists():
                    for subfeature in subfeatures:
                        subfeatures_list.append(subfeature)

    project_view_context = {
        "projects": projects_list,
        "features": features_list,
        "subfeatures": subfeatures_list,
        "username": username,
    }
    return render(
        request, "brainstorm_tools/projects.html", context=project_view_context
    )
