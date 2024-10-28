# seasense_backend/urls.py

from django.urls import path
from .views import StatesByRegionView, AllRegionsView

urlpatterns = [
    path('regions/', AllRegionsView.as_view(), name='all_regions'),  # Lists all regions
    path('states/<int:region_id>/', StatesByRegionView.as_view(), name='states_by_region'),  # Fetches states by region ID
]
