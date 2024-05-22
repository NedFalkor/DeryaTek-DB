from django.apps import AppConfig


class DtBandsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dt_bands'

    def ready(self):
        import dt_bands.bands_admin
