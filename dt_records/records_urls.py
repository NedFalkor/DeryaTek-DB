from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .CRUD.record_crud import RecordCRUD
from .CRUD.label_crud import LabelCRUD

router = DefaultRouter()
router.register(r'records', RecordCRUD, basename='records')
router.register(r'labels', LabelCRUD, basename='labels')

urlpatterns = [
    path('api/', include(router.urls)),
]
