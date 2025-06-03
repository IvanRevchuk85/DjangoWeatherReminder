import requests
from django.core.mail import send_mail


# Sending notifications to a subscriber
def notify_subscriber(user, weather_data, send_email=False, send_webhook=False, webhook_url=None):
    """
        Sends a notification to the user via email and/or webhook
        :param user: user object (user.email, user.username)
        :param weather_data: weather dictionary (city, temperature, humidity, description)
        :param send_email: if True — send email
        :param send_webhook: if True — send webhook
        :param webhook_url: webhook address
    """
    # Forming a message
    subject = f"🌦 Weather in {weather_data['city']}"
    message = f"Temperature: {weather_data['temperature']}°C\n" \
        f"Humidity: {weather_data['humidity']}%\n" \
        f"Description: {weather_data['description']}"

    # Email
    if send_email:
        print(f"📬 Sending an email to {user.email}")

        send_mail(
            subject,
            message,
            'weather@reminder.com',  # От кого
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
            print(f"❌ Error sending webhook for {user.username}: {e}")
