import numpy as np

WINDOW_SIZE = 25
PREAMBLE = 25

""" Cumulative sum to find all possible contiguous sums in a list """


def load_data():
    with open('./input.txt') as fp:
        file = fp.read()
    return file.splitlines()


def check_rule(result, previous_list):
    candidates = [i for i in previous_list if i < result]  # Bigger are useless.
    for x in candidates:
        if result - x in candidates:
            if x == result / 2:  # Same number, is it here twice?
                nr_occurences = sum([i == x for i in candidates])
                if nr_occurences > 1:
                    return True
                else:
                    continue
            else:
                return True
        else:
            continue
    else:
        return False


def task1(codes):
    for i in range(PREAMBLE, len(codes)):
        current_nr = codes[i]
        previous_list = codes[(i - WINDOW_SIZE):i]
        if check_rule(current_nr, previous_list):
            continue
        else:
            print(current_nr)
            break


def task2(codes, result):
    codes = np.array(codes)
    cumsum = np.cumsum(codes)

    if (cumsum == result).sum():
        result_reached = np.where(cumsum == result)[0][0]
        return codes[:result_reached + 1]
    else:
        for i, x in enumerate(codes):
            cumsum -= x
            if (cumsum == result).sum():
                result_reached = np.where(cumsum == result)[0][0]
                return codes[i + 1:result_reached + 1]
        else:
            print('NOTHING FOUND')


codes = list(map(int, load_data()))
task1(codes)

sum_to_result = task2(codes, 507622668)
assert sum_to_result.sum() == 507622668
print(sum_to_result.min() + sum_to_result.max())
