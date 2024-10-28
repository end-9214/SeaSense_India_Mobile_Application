# seasense_backend/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Region
from .serializers import RegionSerializer

# View to fetch all regions with their states and beaches
class AllRegionsView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)

# View for fetching states by a specific region using region_id
class StatesByRegionView(APIView):
    def get(self, request, region_id):
        try:
            region = Region.objects.get(id=region_id)
            serializer = RegionSerializer(region)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Region.DoesNotExist:
            return Response({"error": "Region not found"}, status=status.HTTP_404_NOT_FOUND)
