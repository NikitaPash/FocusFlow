from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("allauth.urls")),
    # path('brainstorm-tools/', include('brainstorm_tools.urls')),
    # path('development-dashboard/', include('development_dashboard')),
    path("", include("homepage_and_profile.urls")),
    # path('notifications/', include('notifications.urls')),
    path("user-auth/", include("user_auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
