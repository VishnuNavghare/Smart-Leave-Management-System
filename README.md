# Smart Leave Management System

A web-based Leave Management System developed using **Python, Django, and MySQL**. This application helps organizations manage employee leave requests efficiently. Employees can apply for leave, track leave status, and update their profiles, while administrators can manage employees and approve or reject leave requests.

---

## 🚀 Features

### Employee Module
- Employee Login
- Employee Dashboard
- Apply for Leave
- View Leave History
- Edit Profile
- Session-based Authentication

### Admin Module
- Admin Login (Django Admin Panel)
- Add Employee
- Edit Employee
- Delete Employee
- View All Leave Requests
- Approve Leave
- Reject Leave

---

## 🛠 Technologies Used

- Python 3.x
- Django
- MySQL
- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Django ORM

---

## 📂 Project Structure

```text
Smart Leave Management System/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
├── leave_app/
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── dashboard.html
│   ├── apply_leave.html
│   ├── leave_history.html
│   ├── profile.html
│   └── ...
│
├── Screenshots/
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

### Clone the Repository

```bash
git clone https://github.com/VishnuNavghare/Smart-Leave-Management-System.git
```

### Move to Project Folder

```bash
cd Smart-Leave-Management-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL Database

Update your **settings.py** database configuration.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'leave_management',
        'USER': 'root',
        'PASSWORD': 'Vishnu@2001',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

## 📸 Screenshots

- Employee Login
- Dashboard
- Apply Leave
- Leave History
- Edit Profile
- Admin Panel

---

## 📦 API Endpoints

```
/api/employees/
/api/leaves/
```

---

## 📁 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Developed By

**Vishnu K. Navghare**

Python Full Stack Developer

---

## 📜 License

This project is developed for educational and placement purposes.