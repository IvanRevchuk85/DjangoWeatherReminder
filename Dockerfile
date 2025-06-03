# 🐍 Use official Python 3.12 image
FROM python:3.12-slim

# 📁 Set working directory inside the container
WORKDIR /app

# 🔁 Copy dependencies file
COPY requirements.txt .

# 📦 Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# 🔁 Copy all project files
COPY . .

# 🔧 Disable .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 🚀 Collect static files and start the server on container launch
RUN python manage.py collectstatic --noinput
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
