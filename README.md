# 🏥 Automated Health Clinic Management API

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-REST_API-092E20?style=for-the-badge&logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)

A robust backend REST API built to manage clinic operations, handle patient registration, and safely schedule appointments. This system features strict data integrity checks to prevent scheduling conflicts and double-bookings.

---

## ✨ Features
* **Patient Registration:** Securely register new patients and automatically generate unique Patient IDs.
* **Appointment Scheduling:** Book appointments linked directly to specific patients.
* **Data Integrity Protocol:** Programmatic safety checks that block double-booking by verifying calendar availability before saving to the database.
* **Admin Dashboard:** Fully integrated Django Admin panel for visual data management.

---

## 🚀 Tech Stack
* **Language:** Python 3
* **Framework:** Django 
* **Database:** SQLite3
* **Testing:** Thunder Client / Postman

---

## ⚙️ Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kaiffarooqui970/Clinic-Management-API.git](https://github.com/kaiffarooqui970/Clinic-Management-API.git)
   cd Clinic-Management-API
