# 🏥 Clinic Management API

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Week_2_Complete-success.svg)

A robust, RESTful backend API built with Django for managing patient records, medical history, prescriptions, and clinic billing. Designed with relational database principles to ensure strict data integrity and efficient querying.

---

## 🏗️ System Architecture & Database Design

This system is built using **Third Normal Form (3NF)** relational database principles. 
* **Custom Unique Identifiers:** Implements custom `save()` logic to auto-generate unique `PAT-` IDs (UUIDs) for every patient, preventing duplicate entry conflicts.
* **Referential Integrity:** Utilizes `ForeignKey` (One-to-Many) and `OneToOneField` (One-to-One) relationships with `CASCADE` deletion to prevent orphaned data.
* **Data Aggregation:** Features a unified history endpoint that joins data across multiple transactional tables (Medical, Prescription, Billing) into a single JSON payload.


---

## 🚀 Local Installation & Setup

To run this project locally on your machine, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/kaif-ahmed-farooqui/Clinic-Management-API.git](https://github.com/kaif-ahmed-farooqui/Clinic-Management-API.git)
cd clinic_management
