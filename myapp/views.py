from rest_framework import viewsets
from rest_framework.response import Response
from .models import Vehicle, RepairJob
from .serializers import VehicleSerializer, RepairJobSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class RepairJobViewSet(viewsets.ModelViewSet):
    queryset = RepairJob.objects.all()
    serializer_class = RepairJobSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for item in data:
            vehicle = Vehicle.objects.get(id=item['vehicle'])
            item['title'] = f"{item['description']} ({vehicle.make} {vehicle.model})"
        return Response(data)