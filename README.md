# Django Welcome Page Project

A simple Django project showing a welcome page with styling.

## Project Status

✅ Successfully installed and running

![Django installation](https://github.com/Weakcods/django-crud/blob/03b1e51b51cc0cb692dcad58d96cd33d71b5e92d/assets/pic-dj.PNG)

## Setup Instructions

1. Activate virtual environment:
```bash
myenv\Scripts\activate.bat
```

2. Navigate to project directory:
```bash
cd try
```

3. Run development server:
```bash
python manage.py runserver
```

4. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

```
dj/                         # Root directory
├── myenv/                  # Virtual environment
├── try/                    # Project directory
    ├── manage.py          # Django management script
    ├── templates/         # HTML templates
    │   └── welcome.html   # Welcome page template
    ├── static/            # Static files
    │   └── css/          # CSS stylesheets
    │       └── style.css # Styles for welcome page
    └── try/              # Project configuration
        ├── settings.py   # Project settings
        ├── urls.py       # URL configurations
        └── ...          # Other Django files
```

## Key Files

- `templates/welcome.html` - Main welcome page template
- `static/css/style.css` - Styling for welcome page
- `try/settings.py` - Project configuration
- `try/urls.py` - URL routing


