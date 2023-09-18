from django.urls import path, include, re_path

from backend_api.views import *
from rest_framework import routers
from django.urls import path

from . import views
from .views import validate_token

router = routers.SimpleRouter()
# router.register(r'task', TaskViewSet)
router.register(r'found_data', FoundDataViewSet)

urlpatterns = [
    path('', views.index),
    path('', include(router.urls)),

    path('validate-token/', validate_token, name='validate-token'),   # ???????? ?? ?????????? ??????
    path('user_tokens/', UserTokenView.as_view(), name='user_tokens'),  # ???????? ?????


    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('task/', TaskViewSet.as_view(), name='tasks-create'),
    path('task/<int:pk>/', TaskViewSetDetailView.as_view(), name='tasks-create'),

    path('drf-auth/', include('rest_framework.urls')),
    # path('create_json_response_to_parser/', views.create_json_response_to_parser, name='serialize_and_save_to_json'),
]
