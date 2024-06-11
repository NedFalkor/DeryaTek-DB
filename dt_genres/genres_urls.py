from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .CRUD.genre_crud import GenreCRUD
from .CRUD.style_crud import StyleCRUD

router = DefaultRouter()
router.register(r'genres', GenreCRUD, basename='genres')
router.register(r'styles', StyleCRUD, basename='styles')

urlpatterns = [
    path('api/', include(router.urls)),
]

