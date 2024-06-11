from django.contrib import admin
from django.utils.html import format_html
from dt_bands.models.band_member import BandMember
from dt_bands.models.band import Band
from dt_bands.models.instrument import Instrument


class BandMemberAdmin(admin.ModelAdmin):
    list_display = (
        'band_member_first_name',
        'band_member_last_name',
        'band_member_birth_year',
        'band_member_death_year',
        'band_member_birth_city',
        'band_member_birth_country',
        'band_member_nationality',
        'get_instruments',
        'display_photo'
    )
    search_fields = (
        'band_member_first_name',
        'band_member_last_name',
        'band_member_birth_city',
        'band_member_nationality',
    )
    list_filter = ('band_member_nationality',
                   'band_member_first_name',
                   'band_member_last_name',
                   'band_member_birth_city',
                   'band_member_birth_year',
                   'band_member_death_year',
                   'band_member_birth_country',)

    def get_instruments(self, obj):
        return ", ".join([instrument.instrument_name for instrument in obj.band_member_instruments.all()])

    get_instruments.short_description = 'Instruments'

    def display_photo(self, obj):
        if obj.band_member_photo:
            return format_html('<img src="{}" width="75x"/>', obj.band_member_photo.url)
        return "No Image"

    display_photo.short_description = 'Photo'


admin.site.register(BandMember, BandMemberAdmin)


class BandAdmin(admin.ModelAdmin):
    list_display = (
        'band_name', 'band_country', 'band_formed_in', 'band_genre', 'band_status', 'band_separation_date',
        'display_photo'
    )
    search_fields = ('band_name', 'band_country')
    list_filter = ('band_country', 'band_genre', 'band_status')

    def display_photo(self, obj):
        if obj.band_photo:
            return format_html('<img src="{}" width="50px"/>', obj.band_photo.url)
        return "No Image"

    display_photo.short_description = 'Photo'


admin.site.register(Band, BandAdmin)


class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('instrument_name', 'instrument_category')
    search_fields = ('instrument_name',)
    list_filter = ('instrument_category',)


admin.site.register(Instrument, InstrumentAdmin)
