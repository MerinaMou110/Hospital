from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User, PatientRecords, Department
from .serializers import PatientRecordsSerializer, DepartmentSerializer, UserSerializer
from .permissions import IsDoctor, IsOwnerOrDoctor, IsPatient
from rest_framework.permissions import IsAuthenticated  # Add this line
from django.core.exceptions import PermissionDenied

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from .models import User
from .serializers import UserSerializer
from .permissions import IsDoctor

class DoctorListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='doctor')
    serializer_class = UserSerializer
    # permission_classes = [IsDoctor]

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='doctor')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

    def get_object(self):
        obj = super().get_object()
        if self.request.user == obj or self.request.user.role == 'doctor':
            return obj
        raise PermissionDenied("You do not have permission to access this doctor.")

class PatientListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(role='patient')
    serializer_class = UserSerializer
    # permission_classes = [IsDoctor]

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='patient')
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrDoctor]

    def get_object(self):
        return self.request.user if self.request.user.role == 'patient' else super().get_object()

class PatientRecordsListView(generics.ListCreateAPIView):
    queryset = PatientRecords.objects.all()
    serializer_class = PatientRecordsSerializer
    permission_classes = [IsDoctor]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'doctor':
            return PatientRecords.objects.filter(department__in=user.departments.all())
        elif user.role == 'patient':
            return PatientRecords.objects.filter(patient=user)
        return PatientRecords.objects.none()

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class PatientRecordsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientRecords.objects.all()
    serializer_class = PatientRecordsSerializer
    permission_classes = [IsOwnerOrDoctor]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'doctor':
            return PatientRecords.objects.filter(department__in=user.departments.all())
        elif user.role == 'patient':
            return PatientRecords.objects.filter(patient=user)
        return PatientRecords.objects.none()

class DepartmentListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

class DepartmentDetailView(generics.RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsDoctor]

    def get_queryset(self):
        return Department.objects.all()

class DepartmentDoctorsListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsDoctor]

    def get_queryset(self):
        department_id = self.kwargs['pk']
        return User.objects.filter(role='doctor', department__id=department_id)

class DepartmentPatientsListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsDoctor]

    def get_queryset(self):
        department_id = self.kwargs['pk']
        return User.objects.filter(role='patient', department__id=department_id)
