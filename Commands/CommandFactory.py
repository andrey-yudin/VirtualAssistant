import sys

from Commands.AbstractCommand import AbstractCommand
from Commands.CurrencyConverterCommand import CurrencyConverterCommand
from Commands.EquationSolveCommand import EquationSolveCommand
from Commands.GetWeatherCommand import GetWeatherCommand
from Commands.ReminderCommand import ReminderCommand


class CommandFactory(object):
    class __HelpCommand(AbstractCommand):
        def __init__(self, factory):
            self._factory = factory

        @property
        def name(self) -> str:
            return 'HELP'

        @property
        def help(self) -> str:
            return 'Выводит справку'

        def command_exist(self, command: str) -> bool:
            return command == self.name

        def execute(self):
            try:
                for command in self._factory.commands:
                    print(f'{command.name}: {command.help}')
            except NotImplementedError:
                pass

    class __UnknownCommand(AbstractCommand):
        def __init__(self):
            self._command = None

        @property
        def name(self) -> str:
            raise NotImplementedError

        @property
        def help(self) -> str:
            raise NotImplementedError

        def command_exist(self, command: str) -> bool:
            self._command = command
            return True

        def execute(self):
            sys.stdout.write(f'Неподдерживаемая команда: "{self._command}".\n')

    def __init__(self):
        self.commands = [
            CurrencyConverterCommand(),
            EquationSolveCommand(),
            GetWeatherCommand(),
            ReminderCommand(),
            self.__HelpCommand(self),
            self.__UnknownCommand(),
        ]

    def get_command(self, line: str) -> AbstractCommand:
        for command in self.commands:
            if command.command_exist(line):
                return command
