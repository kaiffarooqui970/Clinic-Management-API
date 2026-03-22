from django.db import models  # THIS LINE FIXES YOUR ERROR!
import uuid

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patient_number = models.CharField(max_length=20, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.patient_number:
            unique_id = uuid.uuid4().hex[:8].upper()
            self.patient_number = f"PAT-{unique_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.patient_number})"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason_for_visit = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Scheduled')

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='records')
    date_recorded = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    symptoms = models.TextField()
    notes = models.TextField(blank=True, null=True)

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    medication_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()
    prescribed_on = models.DateField(auto_now_add=True)

# --- BILLING & INSURANCE ---

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='invoices')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    billing_date = models.DateField(auto_now_add=True)

class InsuranceClaim(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    insurance_provider = models.CharField(max_length=200)
    policy_number = models.CharField(max_length=100)
    claim_status = models.CharField(max_length=50, default='Pending')