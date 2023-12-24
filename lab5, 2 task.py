import requests
from tkinter import Tk
from tkinter.ttk import Label

CITY = 'Saint-Petersburg'
COUNTRY = 'Russia'
LANGUAGE = 'ru'
TOKEN = 'b2ca9dc25be7d54a725eb797d5821fc1'
HEIGHT = 720
WIDTH = 1280
 

class WeatherAPI:

    token = ''
    base_url = 'http://api.openweathermap.org'
    coord_url = '/geo/1.0/direct'
    weather_url = '/data/2.5/weather'

    def __init__(self, city=CITY, country=COUNTRY, lg=LANGUAGE):
        self.city = city
        self.country = country
        self.language = lg

    def request_details(self):
        params = {
            'q': f'{self.city},{ self.country}',
            'limit': 1,
            'appid': self.token
            }
        url = f'{self.base_url}{self.coord_url}'
        details = requests.get(url, params=params)
        data = details.json()[0]
        self.retrieve_coordinates(data)

    def retrieve_coordinates(self, data):
        self.latitude = data['lat']
        self.longitude = data['lon']

    def request_weather(self):
        params = {
             'lat': self.latitude,
             'lon': self.longitude,
             'units': 'metric',
             'appid': self.token,
             'lang': self.language
         }
        url = f'{self.base_url}{self.weather_url}'
        weather = requests.get(url, params=params)
        self.weather = weather.json()
    
    def string_weather(self):
        city = self.weather['name']
        temp = self.weather['main']['temp']
        humidity = self.weather['main']['humidity']
        pressure = self.weather['main']['pressure']
        data = self.weather['weather'][0]
        details = data['description'].capitalize()
        information = f'{city} {temp}°C,\n{details}\nВлажность: {humidity} %\nДавление: {pressure} гПа'
        return information

    def show_page(self):
        text = self.string_weather()
        window = Tk()
        window.title("Добро пожаловать в самое прекрасное приложение!")
        window.geometry(f'{WIDTH}x{HEIGHT}')
        label = Label(window, text=text, font=("Times new Roman", 25))
        label.grid(column=0, row=0)
        window.mainloop()


if __name__ == '__main__':
    WeatherAPI.token = TOKEN
    weather = WeatherAPI()
    weather.request_details()
    weather.request_weather()
    weather.show_page()