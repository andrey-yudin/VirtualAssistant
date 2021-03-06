import os
import sys

from configparser import ConfigParser


class ApplicationSettings(object):
    _organization_name = 'VirtualAssistantApp'
    _config_file_name = 'VirtualAssistantApp.conf'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        self._config = ConfigParser()

        if not os.path.exists(self._local_config_path()):
            self._create_default_local_config()

        self._config.read(self._local_config_path())

    @property
    def person_city(self):
        return self._get_value('CommonSettings', 'City')

    @property
    def weather_api_key(self):
        return self._get_value('Weather', 'api_key')

    def _create_default_local_config(self):
        self._config['CommonSettings'] = {}
        self._config['CommonSettings']['city'] = str("Tomsk, RU")

        self._config['Weather'] = {}
        self._config['Weather']['api_key'] = str("221240ff2b98de0a1e4f018c05e0a459")

        path = self._local_config_path()
        basedir = os.path.dirname(path)

        if not os.path.exists(basedir):
            os.makedirs(basedir)

        with open(path, 'w') as config_file:
            self._config.write(config_file)

    def _get_value(self, section, key):
        try:
            return self._config[section][key]
        except KeyError:
            print('Недопустимый файл конфигурации')
            sys.exit(1)

    @staticmethod
    def _home_directory():
        return os.path.expanduser('~')

    @classmethod
    def _local_config_path(cls):
        return os.path.join(
            cls._home_directory(),
            '.config',
            cls._organization_name,
            cls._config_file_name
        )
