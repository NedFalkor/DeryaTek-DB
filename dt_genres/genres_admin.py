from django.contrib import admin
from django.utils.html import format_html
from dt_genres.models.genre import Genre
from dt_genres.models.style import Style
from dt_genres.models.sub_genre import SubGenre


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_name', 'genre_description', 'get_genre_photo')
    search_fields = ('genre_name',)
    list_filter = ('genre_name',)

    def get_genre_photo(self, obj):
        if obj.genre_photo:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.genre_photo.url)
        return "No Photo"

    get_genre_photo.short_description = 'Photo'


class StyleAdmin(admin.ModelAdmin):
    list_display = ('style_name', 'style_description', 'get_style_photo', 'get_genres')
    search_fields = ('style_name', 'style_genres__genre_name')
    list_filter = ('style_genres', 'style_name')
    filter_horizontal = ('style_genres',)

    def get_style_photo(self, obj):
        if obj.style_photo:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.style_photo.url)
        return "No Photo"

    get_style_photo.short_description = 'Photo'

    def get_genres(self, obj):
        return ", ".join([genre.genre_name for genre in obj.style_genres.all()])

    get_genres.short_description = 'Genres'


class SubGenreAdmin(admin.ModelAdmin):
    list_display = ('sub_genre_name', 'sub_genre_description', 'get_sub_genre_photo', 'get_styles')
    search_fields = ('sub_genre_name', 'sub_genre_description', 'sub_genre_styles__style_name')
    list_filter = ('sub_genre_styles', 'sub_genre_name')
    filter_horizontal = ('sub_genre_styles',)

    def get_sub_genre_photo(self, obj):
        if obj.sub_genre_photo:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.sub_genre_photo.url)
        return "No Photo"

    get_sub_genre_photo.short_description = 'Photo'

    def get_styles(self, obj):
        return ", ".join([style.style_name for style in obj.sub_genre_styles.all()])

    get_styles.short_description = 'Styles'


admin.site.register(Genre, GenreAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(SubGenre, SubGenreAdmin)
