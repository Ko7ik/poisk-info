from django.urls import path
from . import views
from backend_api.views import *

urlpatterns = [
    path('', views.index),
    path('found_data/', FoundDataView.as_view(), name='found_data'),
    path('search_data/', SearchDataView.as_view(), name='search_data')
]

