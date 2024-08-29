from rest_framework import permissions

class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'doctor'

class IsPatient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'patient'

class IsOwnerOrDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.patient == request.user or request.user.role == 'doctor'
