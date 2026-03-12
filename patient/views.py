from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
import json
from .models import Patient, Appointment

@csrf_exempt 
def register_patient(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_patient = Patient.objects.create(
                name=data.get('name'),
                address=data.get('address'),
                medical_history=data.get('medical_history')
            )
            return JsonResponse({'message': 'Patient registered successfully!', 'patient_id': new_patient.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

@csrf_exempt
def book_appointment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            patient_id = data.get('patient_id')
            appointment_time_str = data.get('appointment_datetime') 

            if not patient_id or not appointment_time_str:
                return JsonResponse({'error': 'Please provide patient_id and appointment_datetime'}, status=400)

            try:
                patient = Patient.objects.get(id=patient_id)
            except Patient.DoesNotExist:
                return JsonResponse({'error': 'Patient not found. Please register first.'}, status=404)

            appointment_time = parse_datetime(appointment_time_str)

            if Appointment.objects.filter(appointment_datetime=appointment_time).exists():
                return JsonResponse({'error': 'This appointment slot is already taken. Please choose another time.'}, status=409)

            new_appointment = Appointment.objects.create(
                patient=patient,
                appointment_datetime=appointment_time
            )

            return JsonResponse({'message': 'Appointment booked successfully!', 'appointment_id': new_appointment.id, 'patient_name': patient.name, 'datetime': appointment_time_str}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)