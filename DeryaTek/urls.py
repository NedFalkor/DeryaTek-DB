from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dt_bands/', include('dt_bands.bands_urls')),
    path('dt_genres/', include('dt_genres.genres_urls')),
    path('dt_gigs/', include('dt_gigs.gigs_urls')),
    path('dt_records/', include('dt_records.records_urls')),
    path('', include('dt_users.users_urls')),
]

# Add i18n patterns for language chooser
urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
