from celery import shared_task
from django.utils import timezone
from weather_app.services.weather_fetcher import fetch_weather_by_city
from weather_app.services.notification_service import notify_subscriber
from weather_app.models import Subscription

@shared_task
def send_weather_notifications():
    """
    Задача Celery: отправляет уведомления подписчикам
    """
    print("🚀 Начинаем рассылку уведомлений подписчикам")

    now = timezone.now().date()  # Получаем текущую дату
    subscriptions = Subscription.objects.all()  # Получаем все подписки (в будущем можно фильтровать)

    for sub in subscriptions:
        city = sub.city  # Город из подписки
        user = sub.user  # Пользователь, владелец подписки

        # 🛰️ Получаем данные погоды
        data = fetch_weather_by_city(city)

        if data:
            # 🔄 Преобразуем данные в нужный формат
            weather_data = {
                "city": city,
                "temperature": data.get("main", {}).get("temp"),
                "humidity": data.get("main", {}).get("humidity"),
                "description": data.get("weather", [{}])[0].get("description"),
            }

            # 📤 Отправляем уведомление по email/webhook, если нужно
            notify_subscriber(
                user=user,
                weather_data=weather_data,
                send_email=getattr(sub, "send_email", False),  # если включено
                send_webhook=getattr(sub, "send_webhook", False),
                webhook_url=getattr(sub, "webhook_url", None),
            )

            print(f"✅ Уведомление отправлено для {user.username} ({city})")
        else:
            print(f"⚠️ Не удалось получить погоду для {city}")

    print("🏁 Рассылка завершена")