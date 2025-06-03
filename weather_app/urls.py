from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReminderViewSet, SubscriptionViewSet, WeatherDataView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 🌐 Router for ViewSets
router = DefaultRouter()
router.register(r'reminders', ReminderViewSet)        # /api/reminders/
router.register(r'subscriptions', SubscriptionViewSet)  # /api/subscriptions/

urlpatterns = [
    path('', include(router.urls)),  # 🔄 Connecting ViewSets
    path('weather/', WeatherDataView.as_view(),
         name='weather'),  # 🌤️ GET-weather in the city
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # 🔐 Getting a JWT token
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),  # 🔄 Token update
]
