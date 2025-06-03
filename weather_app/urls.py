from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReminderViewSet, SubscriptionViewSet, WeatherDataView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 🌐 Роутер для ViewSet'ов
router = DefaultRouter()
router.register(r'reminders', ReminderViewSet)        # /api/reminders/
router.register(r'subscriptions', SubscriptionViewSet)  # /api/subscriptions/

urlpatterns = [
    path('', include(router.urls)),  # 🔄 Подключаем ViewSet'ы
    path('weather/', WeatherDataView.as_view(), name='weather'),  # 🌤️ GET-погода по городу
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 🔐 Получение JWT токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 🔄 Обновление токена
]
