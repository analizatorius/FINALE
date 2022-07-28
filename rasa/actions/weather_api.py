import requests

def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=686dc4ca7fd16619423f33942223f171"
    json_data = requests.get(url).json()
    format_add = json_data['main']
    return format_add


# print(weather("london"))