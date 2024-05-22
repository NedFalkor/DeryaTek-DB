from django.urls import include, path
from rest_framework.routers import DefaultRouter

from dt_bands.CRUD.band_crud import BandCRUD
from dt_bands.CRUD.band_member_crud import BandMemberCRUD
from dt_bands.CRUD.instrument_crud import InstrumentCRUD

router = DefaultRouter()
router.register(r'bands', BandCRUD, basename='bands')
router.register(r'band_members', BandMemberCRUD, basename='band_members')
router.register(r'instruments', InstrumentCRUD, basename='instruments')

urlpatterns = [
    path('api/', include(router.urls)),
]
