from rest_framework import serializers
from .models import WaterModel


class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterModel
        fields = ('name', 'place', 'createdate', 'telnumber','id','quantity')


