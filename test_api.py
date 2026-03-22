import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"

def run_clinic_audit():
    print("🚀 Starting Clinic API Audit...\n")

    # 1. Test Patient Registration
    patient_data = {
        "name": "Test Patient",
        "address": "Leipzig, Germany",
        "medical_history": "Initial Audit Test"
    }
    
    print("📝 Testing Patient Registration...")
    reg_response = requests.post(f"{BASE_URL}/register/", json=patient_data)
    
    if reg_response.status_code == 201:
        patient_id = reg_response.json().get('patient_id')
        print(f"✅ SUCCESS: Patient created with ID: {patient_id}")
    else:
        print(f"❌ FAILED: Registration returned {reg_response.status_code}")
        return

    # 2. Test Appointment Booking
    appointment_data = {
        "patient_id": patient_id,
        "appointment_datetime": "2026-12-25T10:00:00Z"
    }
    
    print("\n📅 Testing Appointment Booking...")
    book_response = requests.post(f"{BASE_URL}/book/", json=appointment_data)
    
    if book_response.status_code == 201:
        print("✅ SUCCESS: Appointment booked!")
    else:
        print(f"❌ FAILED: Booking returned {book_response.status_code}")

    # 3. Test Data Integrity (The Double Booking Check)
    print("\n🔒 Testing Data Integrity (Double Booking)...")
    conflict_response = requests.post(f"{BASE_URL}/book/", json=appointment_data)
    
    if conflict_response.status_code == 409:
        print("✅ SUCCESS: System blocked double-booking (409 Conflict).")
    else:
        print(f"❌ FAILED: System should have blocked this, but returned {conflict_response.status_code}")

    print("\n🏁 Audit Complete!")

if __name__ == "__main__":
    try:
        run_clinic_audit()
    except requests.exceptions.ConnectionError:
        print("🛑 ERROR: Server is not running! Run 'python3 manage.py runserver' first.")