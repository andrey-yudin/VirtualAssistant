import sys

from Commands.AbstractCommand import AbstractCommand
from currency_converter import CurrencyConverter


class CurrencyConverterCommand(AbstractCommand):
    def __init__(self):
        pass

    @property
    def name(self):
        return 'CONVERTER'

    @property
    def help(self) -> str:
        return 'Конвертер валют'

    def command_exist(self, command: str) -> bool:
        return command == self.name

    def execute(self):
        converter = CurrencyConverter()
        _summa = int(input("Введите сумму для конвертации: \n"))
        _from_currency = input("Введите исходную валюту: \n")
        _target_currency = input("Введите конечную валюту: \n")
        try:
            sys.stdout.write(
                f'Результат конвертации: "{round(converter.convert(_summa, _from_currency, _target_currency),2)}"\n'
            )
        except ValueError:
            sys.stdout.write("Ошибка выполнения функции")
            pass
