from django.contrib import admin
from django.utils.html import format_html

from dt_gigs.models.festival import Festival
from dt_gigs.models.gig import Gig
from dt_gigs.models.venue import Venue
from dt_gigs.models.setlist import Setlist


class SetlistInline(admin.TabularInline):
    model = Setlist
    extra = 1


class GigAdmin(admin.ModelAdmin):
    list_display = ('get_band', 'get_venue', 'gig_date', 'gig_ticket_price', 'display_link')
    list_filter = ('gig_date', 'venue')
    search_fields = ('band__band_name', 'venue__venue_name')
    inlines = [SetlistInline]

    def get_band(self, obj):
        return obj.band.band_name

    get_band.short_description = 'Band'

    def get_venue(self, obj):
        return obj.venue.venue_name

    get_venue.short_description = 'Venue'

    def display_link(self, obj):
        if obj.gig_link:
            return format_html('<a href="{}" target="_blank">Link</a>', obj.gig_link)
        return "No Link"

    display_link.short_description = 'Link'


class SetlistAdmin(admin.ModelAdmin):
    list_display = ('get_gig', 'song_number', 'song_title', 'song_duration', 'album_name')
    list_filter = ('gig', 'album_name')
    search_fields = ('song_title', 'album_name', 'gig__band__band_name', 'gig__venue__venue_name')

    def get_gig(self, obj):
        return f"{obj.gig.band.band_name} at {obj.gig.venue.venue_name}"

    get_gig.short_description = 'Gig'


class FestivalAdmin(admin.ModelAdmin):
    list_display = ('festival_name', 'festival_start_date', 'festival_end_date', 'festival_ticket_price')
    list_filter = ('festival_start_date', 'festival_end_date')
    search_fields = ('festival_name',)
    filter_horizontal = ('venues', 'bands')


class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'venue_address', 'venue_capacity')
    search_fields = ('venue_name', 'venue_address')
    list_filter = ('venue_capacity',)


admin.site.register(Gig, GigAdmin)
admin.site.register(Setlist, SetlistAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Venue, VenueAdmin)
