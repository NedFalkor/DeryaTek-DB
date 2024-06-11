from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .CRUD.gig_crud import GigCRUD
from .CRUD.festival_crud import FestivalCRUD
from .CRUD.setlist_crud import SetlistCRUD
from .CRUD.venue_crud import VenueCRUD

router = DefaultRouter()
router.register(r'gigs', GigCRUD, basename='gig')
router.register(r'festivals', FestivalCRUD, basename='festival')
router.register(r'venues', VenueCRUD, basename='venue')
router.register(r'setlists', SetlistCRUD, basename='setlist')

urlpatterns = [
    path('', include(router.urls)),
]
