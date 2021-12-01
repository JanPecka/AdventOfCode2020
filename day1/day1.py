from itertools import combinations


def task1(exp):
    for i in exp:
        if (2020 - i) in exp:
            return i * (2020 - i)


def task2_combinations(exp):
    """137 ms ± 12.1 ms"""
    for i, j, k in combinations(exp, 3):
        if (i + j + k) == 2020:
            return i * j * k


def task2_based_on_task1(exp):
    """1.46 ms ± 25.4 µs"""
    min_exp = min(exp)

    for i in exp:
        for j in exp - {i}:
            if i + j > (2020 - min_exp):
                continue
            elif (2020 - i - j) in exp:
                return i * j * (2020 - i - j)


with open('./day1/input.txt') as fp:
    input_txt = fp.read()

expenses = {int(i) for i in input_txt.split('\n')}

print(task1(expenses))

print(task2_combinations(expenses))

print(task2_based_on_task1(expenses))