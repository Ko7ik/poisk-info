from django.urls import path, include, re_path
from . import views

from backend_api.views import *
from rest_framework import routers
from django.urls import path
from .views import validate_token

router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)
router.register(r'found_data', FoundDataViewSet)

urlpatterns = [
    path('', views.index),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('validate-token/', validate_token, name='validate-token'),

    path('drf-auth/', include('rest_framework.urls')),
    path('create_json_response_to_parser/', views.create_json_response_to_parser, name='serialize_and_save_to_json'),
]
