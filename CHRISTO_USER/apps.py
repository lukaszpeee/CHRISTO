from django.apps import AppConfig


class ChristoUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CHRISTO_USER'

    def ready(self):
        import CHRISTO_USER.signals
