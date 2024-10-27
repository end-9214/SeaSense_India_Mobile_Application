# seasense_backend/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Region
from .serializers import RegionSerializer

# View to fetch all regions with their states and beaches
class AllRegionsView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)

# Optional view for fetching states by a specific region (already implemented earlier)
class StatesByRegionView(APIView):
    def get(self, request, region_name):
        try:
            region = Region.objects.get(name__iexact=region_name)
            serializer = RegionSerializer(region)
            return Response(serializer.data)
        except Region.DoesNotExist:
            return Response({"error": "Region not found"}, status=404)
