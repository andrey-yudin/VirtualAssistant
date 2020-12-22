from threading import Thread
from time import sleep
from Commands.CommandFactory import CommandFactory


class ApplicationLogic(object):

    def __init__(self):
        self.factory = CommandFactory()
        self.tasks = list()

    def command_execute_func(self):
        while True:
            line = input('==> ')
            self.factory.get_command(line).execute()
            sleep(1)

    def run_app(self):
        task = Thread(target=self.command_execute_func())
        reminder_task = Thread(target=self.factory.get_command("REMINDER").execute())
        task.start()
        self.tasks.append(task)
        reminder_task.start()
        self.tasks.append(reminder_task)
        for task in self.tasks:
            task.join()
