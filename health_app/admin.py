from django.contrib import admin

# Register your models here.

from .models import User, Department, PatientRecords

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'specialization')
    search_fields = ('name', 'location')

@admin.register(PatientRecords)
class PatientRecordsAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'patient', 'created_date', 'diagnostics', 'observations', 'treatments', 'department')
    list_filter = ('department',)
    search_fields = ('diagnostics', 'observations', 'treatments')
