import requests
from Commands.AbstractCommand import AbstractCommand
from AppLogic.AppSettings import ApplicationSettings


class GetWeatherCommand(AbstractCommand):
    def __init__(self):
        self.application_settings = ApplicationSettings()

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
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={
                                   'id':
                                       self.get_city_id(
                                           self.application_settings.person_city,
                                           self.application_settings.weather_api_key
                                       ),
                                   'units': 'metric',
                                   'lang': 'ru',
                                   'APPID': self.application_settings.weather_api_key
                               }
                               )
            data = res.json()
            print(
                "Погода в городе " + self.application_settings.person_city.split(',', maxsplit=1)[0] + ":" + "\n"
            )
            for i in data['list']:
                print(i['dt_txt'],
                      'Температура: ', '{0:+3.0f}'.format(i['main']['temp']),
                      'Погодные условия: ', i['weather'][0]['description'])
        except Exception as e:
            print('Получено исключение ' + str(e) + '\n')
            print('Проверьте корректность ввода города и API ключа \n')
            pass
