import sys
from sympy import solve, Eq, symbols
from Commands.AbstractCommand import AbstractCommand


class EquationSolveCommand(AbstractCommand):
    def __init__(self):
        self.power = 0
        self.equation_coefficient = list()
        self.equation = 0
        self.x = symbols('x')

    @property
    def name(self):
        return 'SOLVE'

    @property
    def help(self) -> str:
        return 'Решает уравнения относительно одной переменной, вида "a*x**n + b*x**(n-1) + ... + c*x + d = 0"'

    def command_exist(self, command: str) -> bool:
        return command == self.name

    def enter_solver_args(self) -> bool:
        try:
            self.power = int(input('Введите степень уравнения:\n'))
        except ValueError:
            sys.stdout.write('Необходимо ввести целое число\n')
            return False
        for i in range(self.power + 1, 0, -1):
            try:
                if i - 1 != 0:
                    self.equation_coefficient.append(float(input(f'Введите коэффициент при x^{i - 1}\n')))
                else:
                    self.equation_coefficient.append(float(input(f'Введите свободный член:\n')))
            except ValueError:
                sys.stdout.write('Ошибка при вводе коэффициента\n')
                return False
        self.equation = 0
        for i in range(self.power + 1, 0, -1):
            if i - 1 != 0:
                self.equation += self.equation_coefficient[i-self.power-1] * self.x**(i-1)
            else:
                self.equation += self.equation_coefficient[i - self.power - 1]
        return True

    def execute(self):
        if not self.enter_solver_args():
            return
        sys.stdout.write(f'Введенное уравнение: {self.equation} = 0 \n')
        try:
            sys.stdout.write(
                f'Результат решения уравнения: '
                f'"{solve(Eq(self.equation, 0), self.x)}"\n'
            )
        except ValueError:
            sys.stdout.write('Ошибка выполнения функции\n')
            pass
