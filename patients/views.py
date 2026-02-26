from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()   
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Patient.objects.filter(user=self.request.user)

        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)