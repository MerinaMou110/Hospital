from rest_framework import serializers
from .models import User, PatientRecords, Department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'first_name', 'last_name', 'role']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'diagnostics', 'location', 'specialization']


class PatientRecordsSerializer(serializers.ModelSerializer):
    patient = UserSerializer(read_only=True)  # Patients and doctors can view patient details but cannot change them.
    department = DepartmentSerializer(read_only=True)  # Patients and doctors can view department details but cannot change them.

    class Meta:
        model = PatientRecords
        fields = ['record_id', 'patient', 'created_date', 'diagnostics', 'observations', 'treatments', 'department', 'misc']
        read_only_fields = ['patient', 'created_date', 'department']  # Making fields read-only to ensure they cannot be modified.

    def create(self, validated_data):
        # Only allow creation of records by doctors
        request = self.context.get('request')
        if request.user.role != 'doctor':
            raise serializers.ValidationError("Only doctors can create patient records.")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Allow updates to certain fields only by the doctor assigned to the patient
        request = self.context.get('request')
        if request.user.role == 'doctor':
            return super().update(instance, validated_data)
        elif request.user == instance.patient:
            # Patients can only update certain fields (e.g., misc, observations)
            restricted_fields = ['diagnostics', 'treatments', 'department']
            for field in restricted_fields:
                validated_data.pop(field, None)
            return super().update(instance, validated_data)
        else:
            raise serializers.ValidationError("You do not have permission to update this record.")
