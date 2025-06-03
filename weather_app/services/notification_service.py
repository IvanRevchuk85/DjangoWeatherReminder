import requests
from django.core.mail import send_mail


# Отправка уведомлений подписчику
def notify_subscriber(user, weather_data, send_email=False, send_webhook=False, webhook_url=None):
    """
    Отправляет уведомление пользователю по email и/или webhook
    :param user: объект пользователя (user.email, user.username)
    :param weather_data: словарь с погодой (city, temperature, humidity, description)
    :param send_email: если True — отправить email
    :param send_webhook: если True — отправить webhook
    :param webhook_url: адрес вебхука
    """
    # Формируем сообщение
    subject = f"🌦 Погода в {weather_data['city']}"
    message = f"Температура: {weather_data['temperature']}°C\n" \
              f"Влажность: {weather_data['humidity']}%\n" \
              f"Описание: {weather_data['description']}"

    #Email
    if send_email:
        print(f"📬 Отправляем email для {user.email}")

        send_mail(
            subject,
            message,
            'weather@reminder.com', # От кого
            [user.email],          # Кому
            fail_silently=False
        )

    # Webhook
    if send_webhook and webhook_url:
        try:
            response = requests.post(
                webhook_url,
                json={
                    'user': user.username,
                    'city': weather_data['city'],
                    'temperature': weather_data['temperature'],
                    'humidity': weather_data['humidity'],
                    'description': weather_data['description']
                },
                timeout=5
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ Ошибка при отправке webhook для {user.username}: {e}")