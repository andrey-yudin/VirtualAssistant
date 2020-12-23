import requests
import sys
from Commands.AbstractCommand import AbstractCommand
from AppLogic.AppSettings import ApplicationSettings


class GetWeatherCommand(AbstractCommand):
    def __init__(self):
        self.application_settings = ApplicationSettings()
        self.api_key = "221240ff2b98de0a1e4f018c05e0a459"

    @property
    def name(self):
        return 'WEATHER'

    @property
    def help(self) -> str:
        return 'Выдает текущую погоду в городе'

    def command_exist(self, command: str) -> bool:
        return command == self.name

    @staticmethod
    def get_city_id(city: str, api_key: str) -> str:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={
                               'q': city,
                               'type': 'like',
                               'units': 'metric',
                               'APPID': api_key
                           }
                           )
        data = res.json()
        return data['list'][0]['id']

    def execute(self):
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={
                                   'id': self.get_city_id(
                                       self.application_settings.person_city,
                                       self.api_key
                                   ),
                                   'units': 'metric',
                                   'lang': 'ru',
                                   'APPID': self.api_key
                               }
                               )
            data = res.json()
            sys.stdout.write(
                "Погода в городе " + self.application_settings.person_city.split(',', maxsplit=1)[0] + ":" + "\n"
            )
            sys.stdout.write("Погодные условия :" + str(data['weather'][0]['description']) + "\n")
            sys.stdout.write("Температура :" + str(data['main']['temp']) + " по Цельсию\n")
        except ValueError:
            sys.stdout.write("Ошибка выполнения функции \n")
            pass
