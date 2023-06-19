
from django.contrib import admin



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import  LocationViewSet,FilteredRoutesView

router = DefaultRouter()
#router.register(r'routes', FilteredRoutesView)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/routes/', FilteredRoutesView.as_view()),

     path('admin/', admin.site.urls),
]