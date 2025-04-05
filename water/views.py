from .models import WaterModel
from .serializers import WaterSerializer
from rest_framework import generics

# Create your views here.
class WaterlsitView(generics.ListAPIView):
     queryset = WaterModel.objects.all()
     serializer_class = WaterSerializer

class WaterCreatView(generics.CreateAPIView):
    queryset = WaterModel.objects.all()
    serializer_class = WaterSerializer

class WaterDetialView(generics.RetrieveAPIView):
    queryset = WaterModel.objects.all()
    serializer_class = WaterSerializer

class WaterDeleteView(generics.DestroyAPIView):
    queryset = WaterModel.objects.all()
    serializer_class = WaterSerializer

class WaterUpDateView(generics.UpdateAPIView):
    queryset = WaterModel.objects.all()
    serializer_class = WaterSerializer
