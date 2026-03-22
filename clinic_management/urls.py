from django.contrib import admin
from django.urls import path
from patient import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.register_patient, name='register_patient'),
    path('api/record/', views.add_medical_record, name='add_medical_record'),
    path('api/prescription/', views.add_prescription, name='add_prescription'),
    path('api/history/<str:patient_number>/', views.get_patient_history, name='get_patient_history'),
    path('api/invoice/', views.create_invoice, name='create_invoice'),  # Added for Billing
]