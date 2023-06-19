from rest_framework import serializers
from api.models import Location,Routes

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'  