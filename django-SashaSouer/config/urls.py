from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),  # Маршруты приложения backend
    path('api/token/', obtain_auth_token, name='api-token'),  # Маршрут для получения токена
]
