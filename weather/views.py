from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def index(request):
    weather_data = {}
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = "b314c4d4dc2ed68bd971cadd6131ac58"  # Get your API key from OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data['error'] = "City not found."

    return render(request, 'weather/index.html', {'weather_data': weather_data})
