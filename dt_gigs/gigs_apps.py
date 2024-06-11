from django.apps import AppConfig


class DtGigsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dt_gigs'

    def ready(self):
        import dt_gigs.gigs_admin
