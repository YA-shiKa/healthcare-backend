# Healthcare Backend 

## Overview

This project is a Healthcare Backend built using Django and Django REST Framework.
It provides secure JWT-based authentication and APIs to manage patients, doctors, and their mappings.

---

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- JWT (djangorestframework-simplejwt)
- Python

---

## Features

- User Registration & Login (JWT Authentication)
- CRUD Operations for Patients
- CRUD Operations for Doctors
- Patient–Doctor Mapping
- Protected Endpoints
- Environment Variable Configuration

---

## API Endpoints
### Authentication
- POST /api/auth/register/
- POST /api/auth/login/

### Patients
- POST /api/patients/
- GET /api/patients/
- GET /api/patients/<patient_id>/
- PUT /api/patients/<patient_id>/
- DELETE /api/patients/<patient_id>/

### Doctors
- POST /api/doctors/
- GET /api/doctors/
- GET /api/doctors/<doctor_id>/
- PUT /api/doctors/<doctor_id>/
- DELETE /api/doctors/<doctor_id>/

### Mappings
- POST /api/mappings/
- GET /api/mappings/
- GET /api/mappings/patient/<patient_id>
- DELETE /api/mappings/patient/<patient_id>

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YA-shiKa/healthcare-backend
cd healthcare_backend
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file in the project root and add:

```
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

---

## Screenshots

### Register API
![Register](docs/Register.png)
---
### Login API (JWT Token)
![Login](docs/Login.png)
---
### Protected Endpoint (401 Unauthorized)
![401 Unauthorized](docs/401Unauthorized.png)
---
### Create Patient
![Create Patient](docs/CreatePatient.png)
---
### Create Doctor
![Create Doctor](docs/CreateDoctor.png)
---
### Create Mapping (Patient Assigned to Doctor)
![Create Mapping](docs/CreateMapping.png)
---
### Get Doctors by Patient
![Get Doctors By Patient](docs/GetDoctorsByPatient.png)
---
### Django Admin Panel
![Admin Panel](docs/AdminPanel.png)

---
