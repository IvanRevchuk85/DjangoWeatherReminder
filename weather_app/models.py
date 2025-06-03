from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    reminder_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.user.username} at {self.reminder_time} in {self.location}"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Подписчик
    city = models.CharField(max_length=100)  # Город
    period = models.IntegerField(choices=[(1, '1 день'), (2, '3 дня'), (6, '6 дней'), (12, '12 дней')])
    send_email = models.BooleanField(default=True)  # Отправка по email
    send_webhook = models.BooleanField(default=False)  # Отправка по webhook
    webhook_url = models.URLField(blank=True, null=True)  # URL для webhook
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # исправил _ap на _at

    def __str__(self):
        return f"{self.user.username} - {self.city} ({self.period} дн.)"

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C, {self.description}"

