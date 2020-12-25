import plyer
from threading import Thread
from datetime import datetime
from datetime import time
from time import sleep
from Commands.AbstractCommand import AbstractCommand


class Reminder(object):
    def __init__(self, reminder_text: str, reminder_time: time):
        self.text = reminder_text
        self.time = reminder_time

    @property
    def reminder_text(self):
        return self.text

    @property
    def reminder_time(self):
        return self.time


class ReminderCommand(AbstractCommand):
    def __init__(self):
        self.reminders = list()
        self.notify_title = "Напоминалка"
        self.notify_app_name = "VirtualAssistant"
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
        text = str(input('О чём вам напомнить?\n'))
        time_entry = input('Введите время напоминания (в формате часы:минуты):\n')
        try:
            hour, minutes = map(int, time_entry.split(':'))
            _time = time(hour, minutes)
            if _time < datetime.now().time():
                raise ValueError
        except ValueError:
            print("Ошибка при вводе времени\n")
            return False
        reminder = Reminder(text, _time)
        self.reminders.append(reminder)
        self.reminders.sort(key=lambda x: x.time)
        return True

    def send_remind(self):
        while True:
            for reminder in self.reminders:
                if reminder.reminder_time.hour == datetime.now().time().hour and \
                        reminder.reminder_time.minute == datetime.now().time().minute:
                    plyer.notification.notify(
                        message=reminder.reminder_text,
                        app_name=self.notify_app_name,
                        title=self.notify_title,
                    )
                    self.reminders.remove(reminder)
            sleep(1)

    def execute(self):
        if not self.enter_reminder_args():
            return
