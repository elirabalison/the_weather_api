
# The weather API

The weather API provide the minimum, maximum, average and median temperature for a given city and period of time.

## Requirements

Python 3.8

Django 3.2.4

Django REST Framework

## Installation

Clone the repository in your computer

```bash
git clone https://github.com/elirabalison/the_weather_api.git
```

Go to the_weather_api folder and activate the virtual environment

```bash
source .env/bin/activate

```
Run the server locally by typing

```bash
python manage.py runserver --insecure

```
Then go to your browser

```bash
http://127.0.0.1:8000/api/locations/miami/?days=2

```

## Usage

You can change the name of the city and the number of days in the URL to get the minimum, maximum, average and median temperature in a specific location.

Note: The weather API is from https://www.weatherapi.com and with their free plan the number of days is limited to 3.
