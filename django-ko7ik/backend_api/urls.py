from django.urls import path, include
from . import views
from backend_api.views import *

urlpatterns = [
    path('', views.index),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('search_data/', SearchDataList.as_view()),
    path('search_data_detail/<int:pk>/', SearchDataDetailView.as_view()),
    path('found_data/', FoundDataList.as_view()),
    path('found_data_detail/<int:pk>/', FoundDataDetailView.as_view())
]

