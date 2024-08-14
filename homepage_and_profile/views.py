from django.shortcuts import render


def home(request):
    return render(request, 'homepage_and_profile/homepage.html')
