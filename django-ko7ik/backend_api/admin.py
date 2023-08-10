from django.contrib import admin
from .models import search_data
from .models import found_data

admin.site.register(search_data)
admin.site.register(found_data)
