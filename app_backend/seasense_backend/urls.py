# seasense_backend/urls.py

from django.urls import path
from .views import StatesByRegionView, AllRegionsView

urlpatterns = [
    path('regions/', AllRegionsView.as_view(), name='all_regions'),  # Endpoint to list all regions with states and beaches
    path('states/<str:region_name>/', StatesByRegionView.as_view(), name='states_by_region'),  # Optional endpoint to fetch states by region
]
