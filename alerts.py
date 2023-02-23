import requests
import africastalking

# Initialize Africa's Talking SMS API
username = "Kairu1"
api_key = "2b96020ee3722046890aa8a7eb3bba6b2a4a2e3b0aa6cc3b1afd80be1cb11a3a"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

# Set up OpenWeatherMap API
api_key = "6be6833956910313ad6eeb4f6bffa8ef"
city = "Nairobi"  # Replace with desired city

# Get weather information from OpenWeatherMap API
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
weather_response = requests.get(weather_url).json()
weather_description = weather_response["weather"][0]["description"]
temperature = weather_response["main"]["temp"]

# Compose SMS message
sms_message = f"Hello! The weather in {city} is currently {weather_description} with a temperature of {temperature}°C."

# Send SMS message using Africa's Talking SMS API
recipients = ["+254705173729"]  # Replace with desired phone number(s)
try:
    response = sms.send(sms_message, recipients)
    print(response)
except Exception as e:
    print(f"Encountered an error while sending SMS: {str(e)}")
