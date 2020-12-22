import sys
import math

from typing import Tuple, Union
from Commands.AbstractCommand import AbstractCommand


class EquationSolveCommand(AbstractCommand):
    def __init__(self):
        pass

    @property
    def name(self):
        return 'SOLVE'

    @property
    def help(self) -> str:
        return 'Решение квадратного уравнения вида: a*x^2 + b*x + c = 0'

    def command_exist(self, command: str) -> bool:
        return command == self.name

    @staticmethod
    def solve(a: float, b: float, c: float) -> Union[Tuple[float, float], float]:
        d = b ** 2 - 4 * a * c

        return ((-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a),) \
            if (d > 0) else -b / (2 * a) if (d == 0) else None

    def execute(self):
        _a = float(input("Введите коэффициент a: \n"))
        _b = float(input("Введите коэффициент b: \n"))
        _c = float(input("Введите коэффициент c: \n"))
        sys.stdout.write(f'Результат решения уравнения: "{self.solve(_a,_b,_c)}"\n')
