# 🧱 System Architecture — DjangoWeatherReminder

This document describes the system architecture of the DjangoWeatherReminder application using UML class diagram components and text-based module explanation.

---

## 🌐 UML Class Diagram Overview

The following components are present in the system:

---

### 🧍 User

Represents a registered user or third-party service.

**Attributes:**
- `email: string`
- `password: string`
- `authToken: string` (JWT)

**Responsibilities:**
- Subscribe to weather updates
- Unsubscribe from updates
- Edit subscriptions
- Retrieve a list of subscriptions

---

### 📬 EmailNotifier

Handles sending weather updates via email.

**Methods:**
- `sendEmail(email: string, content: string): void`

Used by the system to notify users by email.

---

### 🌐 WebhookNotifier

Used to send notifications to external systems via webhook.

**Methods:**
- `sendWebhook(url: string, payload: string): void`

---

### ☁️ WeatherAPI

External dependency used to fetch real-time weather data.

**Methods:**
- `getWeatherData(city: string): WeatherData`

---

### 🌡 WeatherData

Stores weather parameters retrieved from an external API.

**Attributes:**
- `temperature: float`
- `humidity: int`
- `description: string`

---

### 📄 Subscription

Describes a user's subscription to a specific city with a set notification interval.

**Attributes:**
- `city: string`
- `period: int` (1, 3, 6, or 12 hours)

**Methods:**
- `edit(period: int): void`

---

## 🧾 Summary

The architecture fully supports the storyline from Task 16:

- Registration with JWT token
- Weather subscription per city
- Custom notification periods (1, 3, 6, 12 hours)
- Notifications via email or webhook
- Integration with external weather API

---

##  Архитектура системы — DjangoWeatherReminder

Этот документ описывает архитектуру приложения DjangoWeatherReminder на основе UML-диаграммы классов.

---

### 👤 Пользователь (User)

Представляет пользователя или сторонний сервис.

**Атрибуты:**
- `email: string`
- `password: string`
- `authToken: string` (JWT)

**Ответственность:**
- Подписка на города
- Управление подписками
- Получение списка подписок

---

### 📧 EmailNotifier

Отправляет уведомления по email.

**Метод:**
- `sendEmail(email: string, content: string): void`

---

### 🌍 WebhookNotifier

Отправляет уведомления через webhook для сторонних сервисов.

**Метод:**
- `sendWebhook(url: string, payload: string): void`

---

### ☁️ WeatherAPI

Внешний сервис получения погодных данных (например, OpenWeather).

**Метод:**
- `getWeatherData(city: string): WeatherData`

---

### 🌡 Погодные данные (WeatherData)

Хранит:
- `temperature: float`
- `humidity: int`
- `description: string`

---

### 🔔 Подписка (Subscription)

**Атрибуты:**
- `city: string`
- `period: int` (1, 3, 6, 12 часов)

**Метод:**
- `edit(period: int): void`

---

## 🏁 Вывод

Диаграмма и архитектура полностью соответствуют требованиям задания Task 16 и позволяют реализовать функциональность:
- регистрация и токен,
- подписка на города с интервалами,
- получение и отправка уведомлений,
- интеграция с внешними API.

