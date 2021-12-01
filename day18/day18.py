import re

re_eq = r'([\d.]+) ([+*]) ([\d.]+)'
re_eq_plus = r'([\d.]+) ([+]) ([\d.]+)'

class day18():  # String equations solver

    def __init__(self):
        with open('./input.txt') as fp:
            self.equations = fp.read().splitlines()

    def calculate(self, x, op, y):
        assert op in ['+', '*'], \
            'Wrong input for `calculate`.'
        x, y = float(x), float(y)
        return x + y if op == '+' else x * y

    def extract_outermost_par(self, eq):
        for i, c in enumerate(eq):
            if c != '(':
                continue
            else:
                n_layer = 0
                for j, c in enumerate(eq[i + 1:], start=i + 1):
                    if c == '(':
                        n_layer += 1
                    elif c == ')':
                        if n_layer == 0:
                            return eq[i:j + 1]
                        else:
                            n_layer -= 1
        else:
            print('Could not parse the equation.')

    def solve_parenthesis(self, eq, plus=False):
        par = self.extract_outermost_par(eq)
        par_solution = (self.solve_equation(par[1:-1]) if not plus
                        else self.solve_equation_plus(par[1:-1]))
        eq = eq.replace(par, str(par_solution), 1)
        return eq

    def solve_equation(self, eq):
        while '(' in eq:
            eq = self.solve_parenthesis(eq)
        while '+' in eq or '*' in eq:
            leftmost_eq = re.search(re_eq, eq)
            sol = self.calculate(*leftmost_eq.groups())
            eq = eq.replace(leftmost_eq.group(0), str(sol), 1)
        else:
            return float(eq)

    def solve_equation_plus(self, eq):
        while '(' in eq:
            eq = self.solve_parenthesis(eq, plus=True)
        while '+' in eq:
            plus_eq = re.search(re_eq_plus, eq)
            sol = self.calculate(*plus_eq.groups())
            eq = eq.replace(plus_eq.group(0), str(sol), 1)
        while '*' in eq:
            mult_eq = re.search(re_eq, eq)
            sol = self.calculate(*mult_eq.groups())
            eq = eq.replace(mult_eq.group(0), str(sol), 1)
        else:
            return float(eq)


    def task1(self):
        solutions = [self.solve_equation(eq) for eq in self.equations]
        print(f'The answer is {sum(solutions)}.')

    def task2(self):
        solutions = [self.solve_equation_plus(eq) for eq in self.equations]
        print(f'The answer is {sum(solutions)}.')

solver = day18()
solver.task1()
solver.task2()
