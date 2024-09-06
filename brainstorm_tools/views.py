from allauth.core.internal.httpkit import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ProjectForm, FeatureFormSet, SubFeatureFormSet


@login_required()
def create_project(request):
    project_form = ProjectForm(request.POST or None)
    feature_formset = FeatureFormSet(request.POST or None)
    subfeature_formset = SubFeatureFormSet(request.POST or None)

    if (
        request.method == "POST"
        and project_form.is_valid()
        and feature_formset.is_valid()
        and subfeature_formset.is_valid()
    ):
        project = project_form.save(commit=False)
        project.user = request.user
        project.save()
        features = feature_formset.save(commit=False)
        for feature in features:
            feature.project = project
            feature.save()

            subfeatures = subfeature_formset.save(commit=False)
            for subfeature in subfeatures:
                subfeature.feature = feature
                subfeature.save()
            return redirect(create_project)

    context = {
        "project_form": project_form,
        "feature_formset": feature_formset,
        "subfeature_formset": subfeature_formset,
    }
    return render(request, "brainstorm_tools/create_project.html", context)
