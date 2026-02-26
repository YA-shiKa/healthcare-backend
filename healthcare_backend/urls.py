from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patients.views import PatientViewSet
from doctors.views import DoctorViewSet
from mappings.views import MappingViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'mappings', MappingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/', include(router.urls)),
]