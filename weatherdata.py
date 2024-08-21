import datetime as dt
import requests
import streamlit as st

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = ""

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

st.title("Weather Data App")

CITY = st.text_input("Enter the city name:", "")

if CITY:
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()

    if response.get('main'):
        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

        st.write(f"**Temperature in {CITY}:** {temp_celsius:.2f} °C or {temp_fahrenheit:.2f}°F")
        st.write(f"**Temperature in {CITY} feels like:** {feels_like_celsius:.2f} °C or {feels_like_fahrenheit:.2f}°F")
        st.write(f"**Humidity in {CITY}:** {humidity}%")
        st.write(f"**Wind Speed in {CITY}:** {wind_speed} m/s")
        st.write(f"**General Weather in {CITY}:** {description}.")
        st.write(f"**Sun Rises in {CITY} at:** {sunrise_time} local time.")
        st.write(f"**Sun Sets in {CITY} at:** {sunset_time} local time.")
    else:
        st.error("City not found. Please enter a valid city name.")
