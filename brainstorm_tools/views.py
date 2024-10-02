from allauth.core.internal.httpkit import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse

from user_auth.models import User
from .forms import ProjectForm, ChangeProjectDetailsForm, RatingForm
from .models import Feature, Project, ProjectRating


@login_required
def create_project(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)

        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user
            project.save()

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
        search_query = request.POST.get("search_query", "").strip()
        if search_query:
            projects = Project.objects.filter(
                user=user, title__icontains=search_query
            ).order_by("-pub_date")
        else:
            projects = Project.objects.filter(user=user).order_by("-pub_date")
    else:
        projects = Project.objects.filter(user=user).order_by("-pub_date")

    page = request.GET.get("page", 1)
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


@login_required
def project_details(request, username, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    features = Feature.objects.filter(project=project)
    features_list = []
    details_form = ChangeProjectDetailsForm(instance=project)

    user_rating = ProjectRating.objects.filter(
        project=project, user=request.user,
    ).first()

    rating_form = RatingForm()

    context = {
        "project": project,
        "features": features_list,
        "details_form": details_form,
        "rating_form": rating_form,
        "user_rating": user_rating,
        "total_rating": project.total_rating,
    }

    if features.exists():
        for feature in features:
            features_list.append(feature)

    if request.method == "POST":
        if "detailed_description" in request.POST:
            details_form = ChangeProjectDetailsForm(request.POST, instance=project)
            if details_form.is_valid():
                details_form.save()

        if "rating" in request.POST and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                new_rating = float(rating_form.cleaned_data["rating"])
                if user_rating:
                    user_rating.rating = new_rating
                    user_rating.save()
                else:
                    ProjectRating.objects.create(
                        user=request.user, project=project, rating=new_rating
                    )

                total_ratings = ProjectRating.objects.filter(project=project)
                project.rating_count = total_ratings.count()
                project.total_rating = total_ratings.aggregate(Avg('rating'))['rating__avg']
                project.save()

                return JsonResponse({
                    "user_rating": new_rating,
                    "total_rating": project.total_rating,
                    "rating_count": project.rating_count,
                })

    return render(request, "brainstorm_tools/project_details.html", context)
