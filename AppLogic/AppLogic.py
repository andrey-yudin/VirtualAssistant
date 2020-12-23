import sys
from Commands.CommandFactory import CommandFactory


class ApplicationLogic(object):

    def __init__(self):
        self.factory = CommandFactory()

    def command_execute_func(self):
        while True:
            line = input('==> ')
            self.factory.get_command(line).execute()

    def run_app(self):
        sys.stdout.write('Вас приветсвует вирутальный помощник\n')
        self.command_execute_func()


