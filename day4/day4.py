import re

"""Regex"""


def load_data():
    with open('./day4/input.txt') as fp:
        file = fp.read()
    return file.split('\n\n')


def task1_regex_set(passwords):
    """3.37 ms ± 56.3 µs"""

    desired_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    re_patt = r'(\w+):'

    valid_count = 0
    for p in passwords:

        present_keys = set(re.findall(re_patt, p))

        if not (desired_keys - present_keys):  # Nothing is missing.
            valid_count += 1

    return valid_count


def task1_all(passwords):
    """521 µs ± 16.8 µs"""

    desired_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    valid_count = 0
    for p in passwords:

        if all((key in p for key in desired_keys)):
            valid_count += 1

    return valid_count


def task2_regex(passwords):

    re_patt = re.compile(
        (r"(?=.*byr:(19[2-9][0-9]|200[0-2]))"
         r"(?=.*iyr:(201[0-9]|2020))"
         r"(?=.*eyr:(202[0-9]|2030))"
         r"(?=.*hgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in))"
         r"(?=.*hcl:#[\da-f]{6}\b)"
         r"(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth)\b)"
         r"(?=.*pid:\d{9}\b)"
         ),
        re.DOTALL
    )

    valid_count = 0
    for p in passwords:

        if re_patt.search(p):
            valid_count += 1

    return valid_count


passwords = load_data()
print(task1_regex_set(passwords))
print(task1_all(passwords))

print(task2_regex(passwords))