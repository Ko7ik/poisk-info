from django.urls import path, include, re_path
from . import views
from backend_api.views import *

urlpatterns = [
    path('', views.index),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('search_data/', SearchDataList.as_view()),
    path('search_data/<int:pk>/', SearchDataUpdate.as_view()),
    path('search_data_delete/<int:pk>/', SearchDataDestroy.as_view()),
    path('found_data/', FoundDataList.as_view()),
    path('found_data/<int:pk>/', FoundDataUpdate.as_view()),
    path('found_data_delete/<int:pk>/', FoundDataDestroy.as_view()),
]

