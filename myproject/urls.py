from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import VehicleViewSet, RepairJobViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'repair-jobs', RepairJobViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]