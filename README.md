# 🌦 Django Weather Reminder

Приложение для напоминаний о погоде с подписками на города и автоматическим сбором погодных данных через API OpenWeather.  
Использует: Django + DRF + JWT + Docker + PostgreSQL.

---

## 🚀 Возможности

- Регистрация и авторизация пользователей (JWT).
- Создание напоминаний с указанием города и времени.
- Подписки на периодические уведомления о погоде по email и/или webhook.
- Получение данных о погоде с OpenWeather API.
- Асинхронная рассылка уведомлений через Celery + Redis.
- Тестирование всех ключевых компонентов (модели, сериализаторы, API, сервисы, задачи).
- Docker-инфраструктура с PostgreSQL, Redis, Celery, Django.

---

## 📁 Структура проекта

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

## ⚙️ Установка и запуск

### 🔧 Клонирование проекта

```bash
git clone git@git.foxminded.ua:foxstudent107439/task_17.git
cd django-weather-reminder
```

### 📦 Настройка `.env`

Создай файл `.env` и укажи:

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

## 🐳 Запуск в Docker

```bash
docker-compose up --build
```

Приложение будет доступно по адресу:  
🔗 http://127.0.0.1:8000/

---

## 🔑 JWT Аутентификация

- Получить токен: `POST /api/token/`
- Обновить токен: `POST /api/token/refresh/`

---

## 🔍 API эндпоинты

| Метод | URL                      | Описание                             |
|-------|--------------------------|--------------------------------------|
| GET   | /api/reminders/          | Получить напоминания текущего юзера |
| POST  | /api/reminders/          | Создать напоминание                 |
| GET   | /api/subscriptions/      | Список подписок пользователя       |
| POST  | /api/subscriptions/      | Подписка на город                  |
| GET   | /api/weather/?city=Kyiv  | Получить и сохранить погоду по городу |

---

## 🧪 Тестирование

### Запуск всех тестов в Docker-контейнере:

```bash
docker-compose exec web pytest -v --tb=short
```

### Покрытие кода (если настроен coverage):

```bash
docker-compose exec web pytest --cov=weather_app
```

---

## 🧠 Зависимости

- Python 3.12
- Django 5.1.7
- djangorestframework
- psycopg2-binary
- requests
- python-dotenv
- rest_framework_simplejwt
- whitenoise

---

## ✅ Покрытие тестами

Покрытие реализовано для:

- `models.py`  
- `serializers.py`  
- `views.py`  
- `services/weather_service.py`  
- `urls.py` (неявно через views)

---

## 📄 Лицензия

Этот проект лицензирован под MIT License.

---

## 👨‍💻 Автор

Created with  by Ivan Revchuk  