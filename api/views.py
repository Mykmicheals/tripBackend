from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response



class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class FilteredRoutesView(APIView):
    def post(self, request):
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')

        if not from_location or not to_location:
            return Response({'error': 'Missing parameters'}, status=400)

        routes = Routes.objects.filter(from_location=from_location, to_location=to_location)
        serialized_routes = RouteSerializer(routes, many=True).data

        return Response({'routes': serialized_routes})


class FilteredFixedRoutesView(APIView):
    def post(self, request):
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')

        if not from_location or not to_location:
            return Response({'error': 'Missing parameters'}, status=400)

        routes = FixedRoutes.objects.filter(from_location=from_location, to_location=to_location)
        serialized_routes = FixedRouteSerializer(routes, many=True).data

        return Response({'fixed_routes': serialized_routes})



class FilteredFlyingRoutesView(APIView):
    def post(self, request):
        from_location = request.POST.get('from_location')
        to_location = request.POST.get('to_location')

        if not from_location or not to_location:
            return Response({'error': 'Missing parameters'}, status=400)

        routes = FlyingRoutes.objects.filter(from_location=from_location, to_location=to_location)
        serialized_routes = FlyingRouteSerializer(routes, many=True).data

        return Response({'flying_routes': serialized_routes})






# Create your views here.
