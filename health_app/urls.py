from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('patients/', views.PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patient_records/', views.PatientRecordsListView.as_view(), name='patient-records-list'),
    path('patient_records/<int:pk>/', views.PatientRecordsDetailView.as_view(), name='patient-records-detail'),
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('departments/<int:pk>/doctors/', views.DepartmentDoctorsListView.as_view(), name='department-doctor-list'),
    path('departments/<int:pk>/patients/', views.DepartmentPatientsListView.as_view(), name='department-patient-list'),
]
