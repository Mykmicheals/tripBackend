from rest_framework import serializers
from api.models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'  


class FixedRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedRoutes
        fields = '__all__' 

class FlyingRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlyingRoutes
        fields = '__all__' 

class DirectRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectRoutes
        fields = '__all__' 