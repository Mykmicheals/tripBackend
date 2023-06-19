from django.contrib import admin
from .models import Location,Routes,FixedRoutes,FlyingRoutes,DirectRoutes



admin.site.register(Location)
admin.site.register(Routes)

admin.site.register(FixedRoutes)
admin.site.register(FlyingRoutes)
admin.site.register(DirectRoutes)


# Register your models here.
