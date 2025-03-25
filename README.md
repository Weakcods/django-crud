# Student Organization Management System

A Django-based system for managing students, colleges, programs, and organizations.

## Features

- Dashboard with statistics and modern UI
- Secure Admin Interface:
  - Password required for each session
  - Session expires after 1 hour
  - Session expires when browser closes
- View-only access for regular users:
  - Students
  - Colleges
  - Programs
  - Organizations
  - Organization Members
- Admin-only CRUD operations (through admin interface)

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
- Sample Installed
  <br>
  ![Django installation](https://github.com/Weakcods/django-crud/blob/03b1e51b51cc0cb692dcad58d96cd33d71b5e92d/assets/pic-dj.PNG)
  <br>
3. Navigate to project directory:
```bash
cd try
```

4. Apply migrations:
```bash
python manage.py makemigrations core
python manage.py migrate
```

5. Load initial data:
```bash
python manage.py loaddata core/fixtures/initial_data.json
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

8. Visit:
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin

## Admin Interface Access

1. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

2. Start the development server:
```bash
python manage.py runserver
```

3. Access the admin interface:
   - URL: http://127.0.0.1:8000/admin
   - Login with your superuser credentials
   
4. Available Admin Features:
   - Manage Students
   - Manage Colleges
   - Manage Programs
   - Manage Organizations
   - Manage Organization Members

## Security Features

1. Session Management:
   - Sessions expire after 1 hour of inactivity
   - Sessions expire when browser closes
   - Password required for each admin session

2. User Access Levels:
   - Admin: Full CRUD access through admin interface
   - Regular users: View-only access to lists
   - Unauthenticated users: View-only access

## Project Structure

```
dj/
├── try/                    # Project directory
    ├── core/              # Main application
    │   ├── models.py      # Database models
    │   ├── views.py       # View controllers
    │   ├── urls.py        # URL routing
    │   ├── admin.py       # Admin interface
    │   └── templatetags/  # Custom template filters
    │       └── form_tags.py
    ├── templates/         # HTML templates
    │   ├── base.html      # Base template
    │   └── core/          # Core app templates
    │       ├── dashboard.html
    │       ├── student_list.html
    │       ├── student_form.html
    │       └── student_confirm_delete.html
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

- Dashboard: Enhanced statistics cards with hover effects
- List Views (View-only for regular users):
  - Students List
  - Colleges List
  - Programs List
  - Organizations List
  - Organization Members List
- Admin Interface:
  - Full CRUD operations for all models
  - Secure session management
  - Search and filter capabilities

## URLs

- Dashboard: `/`
- View-only Lists:
  - Students: `/students/`
  - Colleges: `/colleges/`
  - Programs: `/programs/`
  - Organizations: `/organizations/`
  - Organization Members: `/members/`
- Admin Interface: `/admin/`

## UI Features

- Poppins font family
- Responsive design
- Enhanced dashboard cards with hover effects
- Centered navigation menu
- Clean table layouts
- Modern card shadows and transitions


