import numpy as np
from functools import reduce

"""Sliding down the hill."""


def load_data():
    with open('./input.txt') as fp:
        file = fp.read()
    return file.split('\n')


def ride_list(slope, n_down, n_right):
    """198 µs ± 9.81 µs"""

    slope_length = len(slope)
    slope_width = len(slope[0])
    pos = (0, 0)

    nr_trees = 0
    while pos[0] < slope_length - 1:
        pos = (pos[0] + n_down,
               (pos[1] + n_right) % slope_width  # Jump back left.
               )
        is_tree = slope[pos[0]][pos[1]] == '#'
        nr_trees += int(is_tree)

    return nr_trees


def ride_np(slope, n_down, n_right):
    """1.49 ms ± 40.8 µs"""

    slope = np.array([list(row) for row in slope])
    slope_l, slope_w = slope.shape

    pos = (0, 0)
    nr_trees = 0
    while pos[0] < slope_l - 1:
        pos = (pos[0] + n_down,
               (pos[1] + n_right) % slope_w  # Jump back left.
               )
        is_tree = slope[pos] == '#'
        nr_trees += int(is_tree)

    return nr_trees


slope = load_data()

directions = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
trees = (
    map(lambda dirs: ride_list(slope, *dirs), directions)
    )
print(reduce(lambda x, y: x * y, trees, 1))


