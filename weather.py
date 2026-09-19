import requests

city = input("Enter a city: ")

# 1. Find the city
geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {
    "name": city,
    "count": 1
}

geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

location = geo_data["results"][0]

latitude = location["latitude"]
longitude = location["longitude"]
city_name = location["name"]

# 2. Get weather for that city
weather_url = "https://api.open-meteo.com/v1/forecast"

weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

weather_response = requests.get(weather_url, params=weather_params)
weather_data = weather_response.json()

weather = weather_data["current_weather"]

temperature = weather["temperature"]
windspeed = weather["windspeed"]
winddirection = weather["winddirection"]

# 3. Print it nicely
print()
print("Weather in", city_name)
print("Temperature:", temperature, "°C")
print("Wind speed:", windspeed, "km/h")
print("Wind direction:", winddirection, "°")