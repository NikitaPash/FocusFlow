from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('brainstorm-tools/', include('brainstorm_tools.urls')),
    # path('development-dashboard/', include('development_dashboard')),
    # path('', include('homepage_and_profile.urls')),
    # path('notifications/', include('notifications.urls')),
    # path('pomodoro-timer/', include('pomodoro_timer.urls')),
    # path('user-auth/', include('user_auth.urls')),
]
