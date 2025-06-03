from django.contrib import admin
from .models import Reminder, Subscription


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'reminder_time', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('user__username', 'location')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'send_email', 'send_webhook')
    list_filter = ('send_email', 'send_webhook')
    search_fields = ('user__username', 'city')
