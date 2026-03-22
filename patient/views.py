import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # THIS LINE FIXES THE ERROR!
from .models import Patient, Appointment, MedicalRecord, Prescription, Invoice, InsuranceClaim

@csrf_exempt
def register_patient(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            patient = Patient.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name')
            )
            return JsonResponse({'message': 'Success!', 'patient_number': patient.patient_number}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def add_medical_record(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            patient = Patient.objects.get(patient_number=data.get('patient_number'))
            MedicalRecord.objects.create(
                patient=patient,
                diagnosis=data.get('diagnosis'),
                symptoms=data.get('symptoms')
            )
            return JsonResponse({'message': 'Record added!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def add_prescription(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            patient = Patient.objects.get(patient_number=data.get('patient_number'))
            Prescription.objects.create(
                patient=patient,
                medication_name=data.get('medication_name'),
                dosage=data.get('dosage'),
                instructions=data.get('instructions')
            )
            return JsonResponse({'message': 'Prescription added!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def create_invoice(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            patient = Patient.objects.get(patient_number=data.get('patient_number'))
            invoice = Invoice.objects.create(
                patient=patient,
                total_amount=data.get('amount')
            )
            return JsonResponse({'message': 'Invoice generated!', 'invoice_id': invoice.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def get_patient_history(request, patient_number):
    if request.method == 'GET':
        try:
            patient = Patient.objects.get(patient_number=patient_number)
            records = list(patient.records.all().values('date_recorded', 'diagnosis'))
            prescriptions = list(patient.prescriptions.all().values('medication_name', 'dosage'))
            invoices = list(patient.invoices.all().values('total_amount', 'billing_date', 'is_paid'))
            
            return JsonResponse({
                'patient': f"{patient.first_name} {patient.last_name}",
                'history': records,
                'prescriptions': prescriptions,
                'billing': invoices
            }, status=200)
        except Patient.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)