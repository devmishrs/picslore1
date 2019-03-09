from rest_framework import serializers
from location.models import *

class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class PlaceMapSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlaceMap
        fields = '__all__'

class PlaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__' 
