from sympy import solve, sympify
from Commands.AbstractCommand import AbstractCommand


class EquationSolveCommand(AbstractCommand):
    def __init__(self):
        self.equation = None

    @property
    def name(self):
        return 'SOLVE'

    @property
    def help(self) -> str:
        return 'Решает вводимые пользователем уравнения'

    def command_exist(self, command: str) -> bool:
        return command == self.name

    def enter_equation(self) -> bool:
        try:
            self.equation = str(input(f'Введите уравнение: \n'))
        except ValueError:
            print('Обнаружен недопустимый символ в выражении\n')
            return False
        return True

    def execute(self):
        if not self.enter_equation():
            return
        try:
            print(
                f'Результат решения уравнения: '
                f'"{solve(sympify("Eq(" + self.equation.replace("=", ",") + ")"))}"\n'
            )
        except Exception as e:
            print('Получено исключение ' + str(e) + '\n')
            print('Проверьте правильность написания функции;' + '\n' +
                  'Целая и дробная часть чисел должны разделяться точкой \n'
                  )
            print('Для получения справки о дотсупных функциях обратитесь '
                  'на сайт "https://docs.sympy.org/latest/index.html" \n')
            pass
