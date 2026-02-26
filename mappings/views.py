from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import PatientDoctorMapping
from .serializers import MappingSerializer


class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__user=self.request.user
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        patient = serializer.validated_data['patient']
        doctor = serializer.validated_data['doctor']

        if patient.user != request.user:
            raise PermissionDenied("You cannot assign doctors to this patient.")

        mapping = serializer.save()

        return Response(
            {
                "message": f"Patient '{patient.name}' successfully assigned to Doctor '{doctor.name}'.",
                "mapping_id": mapping.id
            },
            status=status.HTTP_201_CREATED
        )
    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def doctors_by_patient(self, request, patient_id=None):
        mappings = self.get_queryset().filter(patient_id=patient_id)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(
            PatientDoctorMapping,
            id=kwargs['pk'],
            patient__user=request.user
        )

        patient_name = instance.patient.name
        doctor_name = instance.doctor.name

        instance.delete()

        return Response(
            {
                "message": f"Doctor '{doctor_name}' successfully unassigned from patient '{patient_name}'."
            },
            status=status.HTTP_200_OK
        )