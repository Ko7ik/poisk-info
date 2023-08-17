from django.urls import path, include, re_path
from . import views
from backend_api.views import *

urlpatterns = [
    path('', views.index),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('task/', TaskList.as_view()),
    path('task_update/<int:pk>/', TaskUpdate.as_view()),
    path('task_delete/<int:pk>/', TaskDelete.as_view()),
    path('found_data/', FoundDataList.as_view()),
    path('found_data_update/<int:pk>/', FoundDataUpdate.as_view()),
    path('found_data_delete/<int:pk>/', FoundDataDestroy.as_view()),
    path('')
]

