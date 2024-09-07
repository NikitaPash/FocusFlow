from allauth.core.internal.httpkit import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ProjectForm
from .models import Feature, SubFeature


@login_required
def create_project(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)

        print(request.POST)

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

                print(f"Feature: {feature_name}, Subfeatures: {subfeatures}")

                for subfeature_name in subfeatures:
                    if subfeature_name.strip():
                        SubFeature.objects.create(
                            feature=feature, subfeature_name=subfeature_name
                        )

                feature_counter += 1

            return redirect("create_project")
    else:
        project_form = ProjectForm()

    context = {
        "project_form": project_form,
    }

    return render(request, "brainstorm_tools/create_project.html", context)
