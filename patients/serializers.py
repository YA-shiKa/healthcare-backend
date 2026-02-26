from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['user']

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be greater than 0.")
        if value > 120:
            raise serializers.ValidationError("Age cannot exceed 120.")
        return value