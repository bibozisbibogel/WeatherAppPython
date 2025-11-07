# Weather App

A simple and elegant desktop weather application built with Python and PyQt5 that fetches real-time weather data from OpenWeatherMap API.

## Features

- Clean and intuitive graphical user interface
- Real-time weather data retrieval
- Temperature display in Celsius
- Weather condition emoji indicators
- Detailed weather descriptions
- Comprehensive error handling for various API and network issues

## Prerequisites

- Python 3.x
- OpenWeatherMap API key (free tier available at [OpenWeatherMap](https://openweathermap.org/api))

## Installation

1. Clone or download this repository

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

## Usage

Run the application:
```bash
python app.py
```

1. Enter the name of any city in the input field
2. Click the "Get Weather" button
3. View the current temperature, weather emoji, and description

## Project Structure

```
WeatherAppPython/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API key)
└── README.md          # Project documentation
```

## Dependencies

- **PyQt5**: GUI framework for creating the desktop application
- **requests**: HTTP library for making API calls to OpenWeatherMap
- **python-dotenv**: Loads environment variables from .env file

## Weather Emojis

The app displays different emojis based on weather conditions:

- ⛈ Thunderstorm
- 🌦 Drizzle
- 🌧 Rain
- ❄ Snow
- 🌫 Fog/Mist
- 🌋 Volcanic ash
- 💨 Squalls
- 🌪 Tornado
- ☀ Clear sky
- ☁ Clouds

## Error Handling

The application handles various error scenarios:
- Invalid city names (404)
- Invalid API key (401)
- Network connection issues
- Server errors (500, 502, 503, 504)
- Request timeouts
- Bad requests (400)

## API

This application uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch weather data.

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.
