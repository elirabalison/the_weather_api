from rest_framework import views
from rest_framework.response import Response

from .serializers import WeatherSerializer

import requests

#function to compute the average temperature
def average_temperature(temperature):
    sum_numbers = 0
    for counter in temperature:
        sum_numbers = sum_numbers + counter
    avg = sum_numbers / len(temperature)
    return avg

#function to compute the median temperature
def median_temperature(temperature):
    n = len(temperature)
    index = n // 2

    if n % 2:
        return sorted(temperature)[index]    

    return sum(sorted(temperature)[index-1:index+1]) / 2

class WeatherView(views.APIView):

    http_method_names = ['get', 'head']

    def get(self, request, city):
        
        #the number of days in parametre
        number_of_days = request.GET.get('days')

        #the url of our API
        url = 'http://api.weatherapi.com/v1/forecast.json?key=b16d544814374b3aa5d03948210107&q='+ city +'&days='+ str(number_of_days) +'&aqi=no'   

        #request the API data and convert the JSON to Python data types
        city_weather = requests.get(url).json()

        #get the content of forecastday dictionnary
        data =  city_weather['forecast']['forecastday']

        #create a list to store data for comparison and calculation
        temperature_max_per_day = []
        temperature_min_per_day = []
        temperature_per_hour = []   
        
        for i in range(0, int(number_of_days)):
            temperature_max_per_day.append(data[i].get('day').get('maxtemp_c'))
            temperature_min_per_day.append(data[i].get('day').get('mintemp_c'))

            for j in range(0,24):
                temperature_per_hour.append((data[i].get('hour'))[j].get('temp_c'))

        weather = {
            'maximum' : max(temperature_max_per_day),
            'minimum' : min(temperature_min_per_day),
            'average' : round(average_temperature(temperature_per_hour),2),        
            'median' : median_temperature(temperature_per_hour),
        }
        result = [weather]

        results = WeatherSerializer(result, many=True).data

        return Response(results)


