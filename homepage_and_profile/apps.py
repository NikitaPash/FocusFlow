from django.apps import AppConfig


class HomepageAndProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "homepage_and_profile"

    def ready(self):
        import homepage_and_profile.signals
