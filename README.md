# 🌦️ Python Weather App

A Python-based weather application that fetches real-time weather information using WeatherAPI and provides voice-based weather reports using Windows Speech API.

## ✨ Features

- Search weather information by city name.
- Fetch real-time weather data using WeatherAPI.
- Display temperature and feels-like temperature.
- Show humidity and wind information.
- Display UV index and precipitation.
- Show local time and weather conditions.
- Convert weather reports into speech.

## 🛠️ Technologies Used

- Python
- Requests
- WeatherAPI
- PyWin32
- Windows Speech API (SAPI)

## 📦 Installation

Install the required dependencies:

```bash
pip install requests pywin32
```

## 🔑 API Configuration

1. Obtain an API key from WeatherAPI.
2. Set it as an environment variable named `WEATHER_API_KEY`.
3. Never upload your API key to GitHub.

## ▶️ How to Run

1. Clone this repository.
2. Open the project folder.
3. Configure your WeatherAPI key.
4. Run the following command:

```bash
python main.py
```

5. Enter the city name when prompted.
6. The application displays and speaks the weather report.

## 📚 What I Learned

- Working with external APIs.
- Making HTTP requests using Python.
- Parsing JSON responses.
- Handling API errors.
- Extracting information from nested dictionaries.
- Integrating text-to-speech functionality.
- Working with external Python libraries.

## ⚠️ Compatibility

The voice functionality uses Windows Speech API through PyWin32 and is designed for Windows environments.
