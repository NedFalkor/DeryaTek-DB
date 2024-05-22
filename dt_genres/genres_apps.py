from django.apps import AppConfig


class DtGenresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dt_genres'

    def ready(self):
        import dt_genres.genres_admin
