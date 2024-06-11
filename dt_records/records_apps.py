from django.apps import AppConfig


class DtRecordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dt_records'

    def ready(self):
        import dt_records.records_admin
