# app_backend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('seasense_backend.urls')),  # Include the seasense_backend app URLs
]
