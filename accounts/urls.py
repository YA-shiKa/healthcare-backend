from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view(permission_classes=[AllowAny])),
]