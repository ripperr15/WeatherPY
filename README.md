# WeatherPY
# CityWeatherPy

CityWeatherPy is a Python-based application designed to provide users with real-time weather information for any city using the OpenWeatherMap API. The application is intuitive and allows users to obtain weather data in either metric or imperial units based on geographical coordinates.

## Features
Fetch and display real-time weather data, including current, maximum, and minimum temperatures.
Customize units to display temperature in Celsius or Fahrenheit.
user-friendly and clear output.
Basic error handling to manage connection errors

## How to Use
1. Clone this repository to your local machine.
2. Navigate to the repository directory via the terminal.
3. Run the Python script using your Python interpreter.
4. Optionally, modify the city name, latitude, longitude, and units to get weather information for different cities.

## Example
```python
myCity = Citi("Toronto", 43.6532, -79.3832)
myCity.printTemp()

newCity = Citi("Dubai", 25.2048, 55.2708, units="imperial")
newCity.printTemp()
Note
Ensure you have a stable internet connection to fetch the weather data.
The OpenWeatherMap API key used here is for demonstration purposes. Please generate your own API key from OpenWeatherMap for extensive usage.
