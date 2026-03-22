from django.contrib import admin
from .models import Patient, Appointment, MedicalRecord, Prescription

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Prescription)