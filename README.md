# Notepad Portal

A web application for storing notes with user authentication. Built with Flask, PostgreSQL, and a fullscreen video background.

## Tech Stack

- **Backend**: Python + Flask (app factory pattern)
- **Database**: PostgreSQL + SQLAlchemy + Flask-Migrate
- **Auth**: Flask-Login + werkzeug password hashing
- **Forms**: Flask-WTF with CSRF protection
- **Frontend**: Jinja2 templates + CSS + vanilla JS
- **Production**: gunicorn

## Local Setup

### Prerequisites
- Python 3.12+
- PostgreSQL

### Install

```bash
# Create database
createdb notepad_db

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask db init
flask db migrate -m "initial"
flask db upgrade

# Run
flask run
```

### Background Video

Place an MP4 video file at `app/static/video/background.mp4`. Short rain/nature clips from [Pexels](https://www.pexels.com/search/videos/rain/) work well (HD, 10-20s, <8MB).

### Environment Variables

Copy `.env.example` to `.env` and configure:

```
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql:///notepad_db
FLASK_CONFIG=production
```

## Deploy

### gunicorn (generic)
```bash
gunicorn wsgi:app
```

### GCP App Engine
```bash
gcloud app deploy app.yaml
```

### Heroku / AWS Elastic Beanstalk
Uses `Procfile` automatically.

## Routes

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Landing page |
| GET/POST | `/auth/register` | Registration |
| GET/POST | `/auth/login` | Login |
| GET | `/auth/logout` | Logout |
| GET | `/notes/` | Dashboard |
| GET/POST | `/notes/create` | Create note |
| GET | `/notes/<id>` | View note |
| GET/POST | `/notes/<id>/edit` | Edit note |
| POST | `/notes/<id>/delete` | Delete note |
