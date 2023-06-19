from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import  LocationViewSet

router = DefaultRouter()
# router.register(r'flights', FlightViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]