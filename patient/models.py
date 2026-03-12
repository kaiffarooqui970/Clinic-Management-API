from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    medical_history = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField()
    
    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.appointment_datetime}"