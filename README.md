# Smart Leave Management System

## Overview

Smart Leave Management System is a web-based application developed using **Python, Django, and MySQL**. It enables employees to apply for leave online and allows administrators to efficiently manage employee records and leave requests.

## Features

* Employee Login
* Employee Dashboard
* Apply for Leave
* View Leave Status
* Admin Login
* Add, Edit, and Delete Employees
* Approve or Reject Leave Requests
* Session-Based Authentication
* MySQL Database Integration
* Responsive User Interface

## Technologies Used

* Python
* Django
* MySQL
* HTML5
* CSS3
* Bootstrap
* JavaScript

## Project Structure

```text
Smart-Leave-Management-System/
│── leave_management/
│── templates/
│── static/
│── manage.py
│── requirements.txt
│── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/VishnuNavghare/Smart-Leave-Management-System.git
```

### 2. Move to the Project Directory

```bash
cd Smart-Leave-Management-System
```

### 3. Create and Activate a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL

Update the database settings in `settings.py` with your MySQL credentials.

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Future Improvements

* Email Notifications
* Leave Balance Management
* Reports and Analytics
* Password Reset
* Employee Profile Management

## Author

**Vishnu Navghare**

* GitHub: https://github.com/VishnuNavghare
* Technology: Python | Django | MySQL
