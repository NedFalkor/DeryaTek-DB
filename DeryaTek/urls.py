from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dt_bands/', include('dt_bands.bands_urls')),
    path('dt_genres/', include('dt_genres.genres_urls')),
    path('dt_records/', include('dt_records.records_urls')),
    path('', include('dt_users.users_urls')),
]
