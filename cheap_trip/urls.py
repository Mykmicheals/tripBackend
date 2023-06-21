
from django.contrib import admin



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import  *

router = DefaultRouter()
#router.register(r'routes', FilteredRoutesView)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/routes/', FilteredRoutesView.as_view()),
    path('api/fixed-routes/', FilteredFixedRoutesView.as_view()),
    path('api/flying-routes/', FilteredFlyingRoutesView.as_view()),



     path('admin/', admin.site.urls),
]