🧱 System Architecture — DjangoWeatherReminder
This document describes the system architecture of the DjangoWeatherReminder application using a UML class diagram and textual component explanations.

🌐 UML Class Diagram Overview
The system includes the following main components:

🧍 User
Represents a registered user or an integrated third-party service.

Attributes:

email: string

password: string

authToken: string (JWT)

Responsibilities:

Subscribe to weather updates

Unsubscribe from notifications

Modify existing subscriptions

Retrieve a list of subscriptions

📬 EmailNotifier
Sends weather update notifications via email.

Methods:

sendEmail(email: string, content: string): void

This component handles communication with users via email.

🌐 WebhookNotifier
Sends weather updates to third-party systems via HTTP webhooks.

Methods:

sendWebhook(url: string, payload: string): void

Used for integrations with external platforms.

☁️ WeatherAPI
External weather provider (e.g., OpenWeatherMap) used to fetch real-time data.

Methods:

getWeatherData(city: string): WeatherData

Handles third-party API calls.

🌡 WeatherData
Represents a set of weather conditions retrieved from an API.

Attributes:

temperature: float

humidity: int

description: string

Used internally by notification services.

📄 Subscription
Describes the user's subscription to weather updates for a specific city.

Attributes:

city: string

period: int (in hours — 1, 3, 6, or 12)

Methods:

edit(period: int): void

Manages subscription settings and update frequency.

🧾 Summary
This architecture was designed in accordance with the requirements of Task 16 and enables:

User registration and JWT-based authentication

Weather subscriptions per city

Flexible notification intervals (1, 3, 6, 12 hours)

Support for both email and webhook notifications

Integration with external weather APIs
