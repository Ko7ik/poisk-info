from django.db import router
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.urls import path, include, re_path

from rest_framework import routers
from django.urls import path

from backend import views
from backend.views import *

urlpatterns = [
    path('', views.index),

    path('validate-token/', validate_token, name='validate-token'),  # ???????? ?? ?????????? ??????
    path('user_tokens/', UserTokenView.as_view(), name='user_tokens'),  # ???????? ?????

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/get_token/', UserTokenView.as_view(), name='api'),

    path('task/', TaskViewSet.as_view(), name='tasks-create'),
    path('task/<int:pk>/', TaskViewSetDetailView.as_view(), name='tasks-edit'),

    path('found_data/', FoundDataViewSet.as_view(), name='found_data-create'),
    path('found_data/<int:pk>/', FoundDataViewSetDetailView.as_view(), name='found_data-edit'),

    path('drf-auth/', include('rest_framework.urls')),
]
