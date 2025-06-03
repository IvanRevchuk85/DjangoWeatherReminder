# 🐍 Используем официальный образ Python 3.12
FROM python:3.12-slim

# 📁 Рабочая директория внутри контейнера
WORKDIR /app

# 🔁 Копируем файл зависимостей
COPY requirements.txt .

# 📦 Установка зависимостей
RUN pip install --upgrade pip && pip install -r requirements.txt

# 🔁 Копируем все файлы проекта
COPY . .

# 🔧 Отключаем .pyc-файлы и буферизацию
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# 🚀 Запуск сервера при старте контейнера
RUN python manage.py collectstatic --noinput
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
