from django.urls import path

from dt_users.CRUD.auth_crud import AuthUserCRUD
from dt_users.CRUD.register_crud import RegisterUserCRUD

urlpatterns = [
    path('auth/', AuthUserCRUD.as_view({
        'post': 'login',
        'get': 'logout',
        'delete': 'delete_account'
    }), name='auth'),

    path('', RegisterUserCRUD.as_view({
        'post': 'create',
        'get': 'list'
    }), name='register'),
]

