from django.db import models
from account.models import User
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    diagnostics = models.TextField()
    location = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PatientRecords(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_records')
    created_date = models.DateTimeField(auto_now_add=True)
    diagnostics = models.TextField()
    observations = models.TextField()
    treatments = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    misc = models.TextField()

    def __str__(self):
        return f'Record {self.record_id} for {self.patient.email}'