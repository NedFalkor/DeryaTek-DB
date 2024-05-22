from django.apps import AppConfig


class DtUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dt_users'

    def ready(self):
        import dt_users.users_admin
