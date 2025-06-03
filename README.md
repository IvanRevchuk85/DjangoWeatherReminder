# 🌦 Django Weather Reminder

A weather reminder application with city-based subscriptions and automatic weather data collection via the OpenWeather API.
Stack: Django + DRF + JWT + Docker + PostgreSQL.

---

## 🚀 Возможности

- User registration and authentication (JWT)
- Creating reminders by city and time
- Subscriptions for periodic weather notifications via email and/or webhook
- Real-time weather data from the OpenWeather API
- Asynchronous notifications via Celery + Redis
- Full testing of all core components (models, serializers, APIs, services, tasks)
- Docker-based infrastructure: PostgreSQL, Redis, Celery, Django

---

## 📁 Project Structure

```
django_weather_reminder/
├── deploy
│   ├── gunicorn.service
│   └── njinx.conf
│   
├── django_weather_reminder/
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── docs/
│   └── uml/
│       └── architecture.md
│
├── staticfiles/
│
├── venv/
│
├── weather_app/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_remove_subscription_updated_ap_and_more.py
│   │   └── 0003_alter_subscription_send_email.py
│   │
│   ├── services/
│   │   ├── notification_service.py
│   │   ├── weather_fetcher.py
│   │   └── weather_service.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_api.py
│   │   ├── test_models.py
│   │   ├── test_notification_service.py
│   │   ├── test_serializers.py
│   │   ├── test_services.py
│   │   ├── test_tasks.py
│   │   ├── test_views.py
│   │   └── test_weather_fetcher.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── urls.py
│   └── views.py
│
├── .dockerignore
├── .env
├── .gitignore
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── pytest.ini
├── README.md
└── requirements.txt

```

---

## ⚙️ Setup & Launch
### 🔧 Clone the project

```
git clone git@git.foxminded.ua:foxstudent107439/task_17.git
cd django-weather-reminder
```

### 📦 Setting `.env`

Create a .env file with the following::

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOST=127.0.0.1,localhost,testserver

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

OPENWEATHER_API_KEY=your_api_key
```

---

## 🐳 Run in Docker

```
docker-compose up --build
```

The application will be available at:  
🔗 http://127.0.0.1:8000/

---

## 🔑 JWT Authentication

- Get token: `POST /api/token/`
- Refresh token: `POST /api/token/refresh/`

---

## 🔍 API эндпоинты

| Method | URL                      | Description                             |
|-------|--------------------------|--------------------------------------|
| GET   | /api/reminders/          | Get reminders for the current user |
| POST  | /api/reminders/          | Create a new reminder                 |
| GET   | /api/subscriptions/      | List of user subscriptions      |
| POST  | /api/subscriptions/      | Subscribe to a city                  |
| GET   | /api/weather/?city=Kyiv  | Get and store weather data by city name |

---

## 🧪 Testing

### Run all tests inside Docker container:

```
docker-compose exec web pytest -v --tb=short
```

### Покрытие кода (если настроен coverage):

```
docker-compose exec web pytest --cov=weather_app
```

---

## 🧠 Dependencies
- Python 3.12
- Django 5.1.7
- djangorestframework
- psycopg2-binary
- requests
- python-dotenv
- rest_framework_simplejwt
- whitenoise

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Created with  by Ivan Revchuk  