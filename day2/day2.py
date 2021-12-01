import re

"""Password validator"""


def load_data():
    with open('./day2/input.txt') as fp:
        file = fp.read()
    return file.split('\n')


def parse_data(lst):
    return [p.split(' ') for p in lst]


def task1_contains():
    """2.57 ms ± 82.8 µs"""
    passwords = parse_data(load_data())

    correct = 0
    for p in passwords:

        allowed_range = p[0].split('-')
        allowed_range = range(int(allowed_range[0]),
                              int(allowed_range[1]) + 1
                              )

        desired_letter = p[1].rstrip(':')

        password = p[2]
        if password.count(desired_letter) in allowed_range:
            correct += 1

    return correct


def task1_regex():
    """47.9 ns ± 3.76 ns"""
    re_exp = r'^(\d+)-(\d+) (\w): (\w+)$'
    passwords = load_data()

    correct = 0
    for p in passwords:

        min_r, max_r, desired_letter, password = re.match(re_exp, p).groups()

        allowed_range = range(int(min_r), int(max_r) + 1)

        if password.count(desired_letter) in allowed_range:
            correct += 1

    return correct


def task2_str():
    """34.5 ns ± 2.22 ns"""
    passwords = parse_data(load_data())

    correct = 0
    for p in passwords:

        specified_places = p[0].split('-')
        desired_letter = p[1].rstrip(':')
        password = p[2]

        if ((password[int(specified_places[0]) - 1] == desired_letter)
            ^ (password[int(specified_places[1]) - 1] == desired_letter)
            ):
            correct += 1

    return correct


def task2_regex():
    """33.7 ns ± 0.874 ns"""
    re_exp = r'^(\d+)-(\d+) (\w): (\w+)$'
    passwords = load_data()

    correct = 0
    for p in passwords:

        place1, place2, desired_letter, password = re.match(re_exp, p).groups()

        if ((password[int(place1) - 1] == desired_letter)
            ^ (password[int(place2) - 1] == desired_letter)
            ):
            correct += 1

    return correct


print(task1_contains())
print(task1_regex())
print(task2_str())