import sys
from sympy import solve, symbols, sympify
from Commands.AbstractCommand import AbstractCommand


class EquationSolveCommand(AbstractCommand):
    def __init__(self):
        self.x = symbols('x')
        self.allowed_symbols = "+-*x0123456789./()= "
        self.equation = None

    @property
    def name(self):
        return 'SOLVE'

    @property
    def help(self) -> str:
        return 'Решает уравнения относительно одной переменной, вида "a*x**n + b*x**(n-1) + ... + c*x + d = 0"'

    def command_exist(self, command: str) -> bool:
        return command == self.name

    def enter_equation(self) -> bool:
        try:
            self.equation = str(input(f'Введите уравнени, используя символы {self.allowed_symbols}:\n'))
            for i in self.equation:
                if i in self.allowed_symbols:
                    pass
                else:
                    raise ValueError
        except ValueError:
            sys.stdout.write('Обнаружен недопустимый символ в выражении\n')
            return False
        return True

    def execute(self):
        if not self.enter_equation():
            return
        try:
            sys.stdout.write(
                f'Результат решения уравнения: '
                f'"{solve(sympify("Eq(" + self.equation.replace("=", ",") + ")"), self.x)}"\n'
            )
        except ValueError:
            sys.stdout.write('Ошибка выполнения функции\n')
            pass
