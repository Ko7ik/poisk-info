from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from backend_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('found_data/', FoundDataView.as_view(), name='found_data'),
    path('search_data/', SearchDataView.as_view(), name='search_data')
]
