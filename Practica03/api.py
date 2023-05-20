import requests
import json
from datetime import datetime

def get_weather():
    city = input('Enter the city you want to search: ')
    API_KEY = "Texto de ejemplo"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.content)
    print(data)
    temperature = data['main']['temp']
    date = datetime.utcfromtimestamp(int(data["dt"])).strftime("%d - %m - %Y %H:%M")
    print('Date: ' + str(date) + ', Temperature: ' + str(temperature))

def weather_last_days():
    num_days = int(input('How many days do you want to query? (up to 5 days): '))
    date_list = []
    for i in range(num_days):
        day = int(input('Enter the day: '))
        month = int(input('Enter the month: '))
        year = int(input('Enter the year: '))
        date = datetime(year, month, day, 9, 0, 0)
        unix_time = date.timestamp()
        API_KEY = "Texto de ejemplo"
        url = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={25.6667}&lon={-100.3167}&units=metric&dt={int(unix_time)}&appid={API_KEY}'
        response = requests.get(url)
        data = json.loads(response.content)
        temperature = data['current']['temp']
        date_list.append(f'{date} Temperature: {temperature} degrees')

    print(date_list)

weather_last_days()

