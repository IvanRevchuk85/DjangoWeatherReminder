from celery import shared_task
from django.utils import timezone
from weather_app.services.weather_fetcher import fetch_weather_by_city
from weather_app.services.notification_service import notify_subscriber
from weather_app.models import Subscription


@shared_task
def send_weather_notifications():
    """
    Celery task: sends notifications to subscribers
    """
    print("🚀 We are starting to send notifications to subscribers")

    now = timezone.now().date()  # We get the current date
    # We receive all subscriptions (in the future you can filter)
    subscriptions = Subscription.objects.all()

    for sub in subscriptions:
        city = sub.city  # City from subscription
        user = sub.user  # User, subscription owner

        # 🛰️ Getting weather data
        data = fetch_weather_by_city(city)

        if data:
            # 🔄 We transform the data into the required format
            weather_data = {
                "city": city,
                "temperature": data.get("main", {}).get("temp"),
                "humidity": data.get("main", {}).get("humidity"),
                "description": data.get("weather", [{}])[0].get("description"),
            }

            # 📤 Send notification via email/webhook if needed
            notify_subscriber(
                user=user,
                weather_data=weather_data,
                send_email=getattr(sub, "send_email", False),  # если включено
                send_webhook=getattr(sub, "send_webhook", False),
                webhook_url=getattr(sub, "webhook_url", None),
            )

            print(f"✅ Notification sent to {user.username} ({city})")
        else:
            print(f"⚠️ Unable to get weather for {city}")

    print("🏁 Mailing completed")
