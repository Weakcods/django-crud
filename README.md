# Student Organization Management System

A Django-based system for managing students, colleges, programs, and organizations.

## Features

- Dashboard with statistics
- CRUD operations for:
  - Students
  - Colleges
  - Programs
  - Organizations
  - Organization Members

## Setup Instructions

1. Create and activate virtual environment:
```bash
python -m venv myenv
myenv\Scripts\activate.bat
```

2. Install dependencies:
```bash
pip install django
```

3. Navigate to project directory:
```bash
cd try
```

4. Apply migrations:
```bash
python manage.py makemigrations core
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

7. Visit:
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin

## Project Structure

```
dj/
├── try/                    # Project directory
    ├── core/              # Main application
    │   ├── models.py      # Database models
    │   ├── views.py       # View controllers
    │   ├── urls.py        # URL routing
    │   └── admin.py       # Admin interface
    ├── templates/         # HTML templates
    │   ├── base.html      # Base template
    │   └── core/          # Core app templates
    │       ├── dashboard.html
    │       └── student_list.html
    ├── static/           # Static files
    │   └── css/          
    │       └── style.css
    └── try/              # Project settings
        ├── settings.py
        └── urls.py
```

## Models

- College: name, code, description
- Program: name, code, description, college (FK)
- Organization: name, code, description
- Student: first_name, last_name, student_id, program (FK)
- OrgMember: student (FK), organization (FK), position

## Views

- Dashboard: Overview with statistics
- List views for all models
- Create forms for all models


