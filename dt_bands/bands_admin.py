from django.contrib import admin

from dt_bands.models import Band, BandMember
from dt_bands.models.instrument import Instrument


class BandAdmin(admin.ModelAdmin):
    list_display = ('band_name', 'band_country', 'band_formed_in', 'band_genre')
    search_fields = ('band_name', 'band_country')
    list_filter = ('band_country', 'band_genre')


class BandMemberAdmin(admin.ModelAdmin):
    list_display = ('band_member_name', 'band_member_birth_year', 'band_member_country', 'band_member_instrument')
    search_fields = ('band_member_name', 'band_member_country')
    list_filter = ('band_member_country', 'band_member_instrument')


class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('instrument_name', 'instrument_category')
    search_fields = ('instrument_name',)
    list_filter = ('instrument_category',)


admin.site.register(Band, BandAdmin)
admin.site.register(BandMember, BandMemberAdmin)
admin.site.register(Instrument, InstrumentAdmin)
