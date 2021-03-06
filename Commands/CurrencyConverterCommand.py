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
        try:
            _summa = float(input("Введите сумму для конвертации: \n"))
        except ValueError:
            print(
                'Ошибка при вводе суммы для конвертации '
                '(для ввода десятичной дроби используйте точку, в качестве разделителя целой и дробной частей)'
                '\n')
            return
        try:
            _from_currency = input("Введите исходную валюту: \n")
            if _from_currency not in converter.currencies:
                raise ValueError
        except ValueError:
            print('Введите исходную валюту в общепринятом формате, например "RUB"\n')
            print('Поддерживаемые валюты:')
            print(*(x for x in converter.currencies), sep='\n')
            print('\n')
            return
        try:
            _target_currency = input("Введите конечную валюту: \n")
            if _target_currency not in converter.currencies:
                raise ValueError
        except ValueError:
            print('Введите конечную валюту в общепринятом формате, например "RUB"\n')
            print('Поддерживаемые валюты:')
            print(*(x for x in converter.currencies), sep='\n')
            print('\n')
            return
        try:
            print(
                f'Результат конвертации: "{round(converter.convert(_summa, _from_currency, _target_currency), 2)}"\n'
            )
        except Exception as e:
            print('Получено исключение ' + str(e) + '\n')
            pass
