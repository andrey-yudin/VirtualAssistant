import sys
import plyer
from threading import Thread
from datetime import datetime
from datetime import time
from time import sleep
from Commands.AbstractCommand import AbstractCommand


class ReminderCommand(AbstractCommand):
    def __init__(self):
        self.reminder_text = None
        self.reminder_time = datetime.now().time()
        self.notify_title = "Напоминалка"
        self.notify_app_name = "VirtualAssistant"
        self.enable_reminder = False
        reminder_task = Thread(target=self.send_remind, daemon=True)
        reminder_task.start()

    @property
    def name(self):
        return 'REMINDER'

    @property
    def help(self) -> str:
        return 'Устанавливает напоминание'

    def command_exist(self, command: str) -> bool:
        return command == self.name

    def enter_reminder_args(self) -> bool:
        self.reminder_text = str(input('О чём вам напомнить?\n'))
        time_entry = input('Введите время напоминания (в формате часы:минуты):\n')
        try:
            hour, minutes = map(int, time_entry.split(':'))
            self.reminder_time = time(hour, minutes)
            if self.reminder_time < datetime.now().time():
                raise ValueError
        except ValueError:
            sys.stdout.write("Ошибка при вводе времени\n")
            return False
        return True

    def send_remind(self):
        while True:
            if self.enable_reminder:
                if self.reminder_time.hour == datetime.now().time().hour and \
                        self.reminder_time.minute == datetime.now().time().minute:
                    plyer.notification.notify(
                        message=self.reminder_text,
                        app_name=self.notify_app_name,
                        title=self.notify_title,
                    )
                    self.enable_reminder = False
            sleep(1)

    def execute(self):
        if not self.enter_reminder_args():
            return
        if not self.enable_reminder:
            self.enable_reminder = True
        else:
            sys.stdout.write('Напоминание уже установлено\n')
            return
