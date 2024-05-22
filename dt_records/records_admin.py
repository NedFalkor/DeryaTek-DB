from django.contrib import admin

from dt_records.models.record import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('record_title', 'record_band', 'record_year', 'record_format', 'record_condition', 'record_type')
    list_filter = ('record_band', 'record_year', 'record_format', 'record_condition', 'record_genre', 'record_type')
    search_fields = ('record_title', 'record_band__name', 'record_genre__name', 'record_label__name')
    raw_id_fields = ('record_band', 'record_genre', 'record_style', 'record_label')
    date_hierarchy = 'record_year'
    ordering = ('record_year', 'record_title')
    fields = (
        ('record_title', 'record_band'),
        'record_cover',
        ('record_genre', 'record_style'),
        ('record_format', 'record_condition', 'record_type'),
        'record_label',
        ('record_tracklist', 'record_tracklist_side_b'),
        'record_year',
    )


admin.site.register(Record, RecordAdmin)
