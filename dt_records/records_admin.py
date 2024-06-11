from django.contrib import admin
from django.utils.html import format_html
from dt_records.models.label import Label
from dt_records.models.record import Record
from dt_records.models.tracklist import Tracklist


class TracklistInline(admin.TabularInline):
    model = Tracklist
    extra = 1


class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'record_title', 'get_band', 'record_year', 'record_format', 'record_condition', 'record_type', 'record_length',
        'get_genres', 'get_sub_genres', 'get_styles', 'get_label', 'get_band_members', 'display_cover')
    list_filter = (
        'record_band', 'record_year', 'record_format', 'record_condition', 'record_type', 'record_label',
        'record_length')
    search_fields = (
        'record_title', 'record_band__band_name', 'record_genres__genre_name', 'record_sub_genres__sub_genre_name',
        'record_styles__style_name', 'record_label__label_name')
    autocomplete_fields = ('record_band', 'record_label')
    filter_horizontal = ('record_genres', 'record_sub_genres', 'record_styles', 'record_band_members',)
    date_hierarchy = 'record_year'
    ordering = ('record_year', 'record_title')
    fields = (
        ('record_title', 'record_band'),
        'record_cover',
        ('record_genres', 'record_sub_genres', 'record_styles'),
        ('record_format', 'record_condition', 'record_type', 'record_length'),
        'record_label',
        'record_year',
        'record_band_members',
    )
    inlines = [TracklistInline]

    def get_band(self, obj):
        return obj.record_band.band_name

    get_band.short_description = 'Band'

    def get_genres(self, obj):
        return ", ".join([genre.genre_name for genre in obj.record_genres.all()])

    get_genres.short_description = 'Genres'

    def get_sub_genres(self, obj):
        return ", ".join([sub_genre.sub_genre_name for sub_genre in obj.record_sub_genres.all()])

    get_sub_genres.short_description = 'Sub-Genres'

    def get_styles(self, obj):
        return ", ".join([style.style_name for style in obj.record_styles.all()])

    get_styles.short_description = 'Styles'

    def get_label(self, obj):
        return obj.record_label.label_name

    get_label.short_description = 'Label'

    def get_band_members(self, obj):
        return ", ".join([f"{member.band_member_first_name} {member.band_member_last_name}" for member in
                          obj.record_band_members.all()])

    get_band_members.short_description = 'Band Members'

    def display_cover(self, obj):
        if obj.record_cover:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.record_cover.url)
        return "No Cover"

    display_cover.short_description = 'Cover'


admin.site.register(Record, RecordAdmin)


class LabelAdmin(admin.ModelAdmin):
    list_display = (
        'label_name', 'label_country', 'label_founding_date', 'label_status', 'display_photo', 'get_genres',
        'get_styles', 'get_sub_genres')
    search_fields = ('label_name', 'label_country')
    list_filter = ('label_status', 'label_country')
    ordering = ('label_name',)
    filter_horizontal = ('label_genres', 'label_styles', 'label_sub_genres',)

    def display_photo(self, obj):
        if obj.label_photo:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.label_photo.url)
        return "No Photo"

    display_photo.short_description = 'Photo'

    def get_genres(self, obj):
        return ", ".join([genre.genre_name for genre in obj.label_genres.all()])

    get_genres.short_description = 'Genres'

    def get_styles(self, obj):
        return ", ".join([style.style_name for style in obj.label_styles.all()])

    get_styles.short_description = 'Styles'

    def get_sub_genres(self, obj):
        return ", ".join([sub_genre.sub_genre_name for sub_genre in obj.label_sub_genres.all()])

    get_sub_genres.short_description = 'Sub-Genres'


admin.site.register(Label, LabelAdmin)
