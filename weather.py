import requests
def Weather(city):
    API_key = "01ab192ce709d3d80cfe2ebe4cda85d2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()
    
    return weather_data['main']