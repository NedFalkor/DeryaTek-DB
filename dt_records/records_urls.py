from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .CRUD.record_crud import RecordCRUD
from .CRUD.label_crud import LabelCRUD
from .CRUD.tracklist_crud import TracklistCRUD

router = DefaultRouter()
router.register(r'records', RecordCRUD, basename='records')
router.register(r'labels', LabelCRUD, basename='labels')
router.register(r'tracklists', TracklistCRUD, basename='tracklists')

urlpatterns = [
    path('api/', include(router.urls)),
]
