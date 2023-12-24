import requests
from tkinter import Tk
from tkinter.ttk import Label, Button
from io import BytesIO
from PIL import ImageTk, Image

CHARACTER = 'Rick Sanchez'
HEIGHT = 720
WIDTH = 1280


class RickandMortyAPI:
    base_url = 'https://rickandmortyapi.com/api'
    character_url = '/character'
    location_url = '/location'

    def __init__(self, name=CHARACTER):
        self.name = name

    def request_character(self):
        params = {
            'name': self.name
        }
        url = f'{self.base_url}{self.character_url}'
        person = requests.get(url, params=params)
        self.character = person.json()

    def string_character(self):
        result = self.character['results'][0]

        gender = result['gender']
        origin = result['origin']['name']
        location = result['location']['name']
        status = result['status']
        picture = result['image']

        response = requests.get(picture)
        self.image = response.content
        self.location = location
        text = (f'Имя: {self.name}\nПол: {gender}'
                f'\nПроисхождение: {origin}\nМестоположение: {location}\n'
                f'Состояние: {status}')

        return text

    def show_page(self):
        text = self.string_character()
        self.window = Tk()
        self.window.title('Lovefinderzz!')
        self.window.geometry(f'{WIDTH}x{HEIGHT}')

        picture = ImageTk.PhotoImage(Image.open(BytesIO(self.image)))
        background = Label(self.window, image=picture)
        background.place(x=0, y=0, relwidth=1, relheight=1)
        label_1page = Label(self.window, text=text, font=('Times new Roman', 25))
        label_1page.grid(column=0, row=0)
        button = Button(self.window, text='Узнать больше о местоположении!', command=self.clicked)
        button.grid(column=0, row=3)
        self.window.mainloop()

    def request_location(self):
        params = {
            'name': self.location
        }
        url = f'{self.base_url}{self.location_url}'
        place = requests.get(url, params=params)
        information = place.json()
        return information

    def clicked(self):
        information = self.request_location()
        result = information['results'][0]
        planet_type = result['type']
        dimension = result['dimension']
        text = f' Планета: {self.location}\n Тип планеты: {planet_type}\n Измерение: {dimension}'
        label_2page = Label(self.window, text=text, font=('Times new Roman', 25))
        label_2page.grid(column=1, row=0)
        self.window.mainloop()


if __name__ == '__main__':
    character = RickandMortyAPI()
    character.request_character()
    character.string_character()
    character.show_page()
    character.request_location()
    character.clicked()
