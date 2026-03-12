# 🏥 Automated Health Clinic Management API

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-REST_API-092E20?style=for-the-badge&logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)

A robust backend REST API built to manage clinic operations, handle patient registration, and safely schedule appointments. This system features strict programmatic data integrity checks to prevent scheduling conflicts and double-bookings.

---

## 🏗️ System Architecture & Data Flow

Below is the sequence diagram illustrating the backend logic used to enforce data integrity during the appointment booking process.

```mermaid
sequenceDiagram
    participant Client as REST Client
    participant API as Django Router
    participant View as views.py
    participant DB as SQLite Database

    Client->>API: POST /api/book/ (ID, Time)
    API->>View: Route Request
    View->>DB: Check if Patient Exists?
    DB-->>View: Returns Status
    View->>DB: Check if Time Slot is Taken?
    
    alt Time Slot Taken
        DB-->>View: Slot Exists
        View-->>Client: 409 Conflict (Error)
    else Time Slot Free
        DB-->>View: Slot Available
        View->>DB: Create Appointment
        DB-->>View: Save Confirmation
        View-->>Client: 201 Created (Success)
    end
