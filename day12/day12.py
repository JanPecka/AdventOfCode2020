import re
import numpy as np

turn_right_transformation = np.array([[0, 1], [-1, 0]])
turn_left_transformation = np.array([[0, -1], [1, 0]])

class day12_task1():  # Ship and waypoint

    def __init__(self):
        self.instructions = self.load_data()
        self.position = np.array((0, 0))
        self.direction = np.array((1, 0))  # East.

    def load_data(self):
        with open('./input.txt') as fp:
            txt = fp.read().splitlines()
        re_patt = r"^(\w)(\d+)$"
        return [re.match(re_patt, i).groups() for i in txt]

    def example1(self):
        re_patt = r"^(\w)(\d+)$"
        self.instructions = [re.match(re_patt, i).groups() for i in
                             ['F10', 'N3', 'F7', 'R90', 'F11']
                             ]
        self.task1()

    def sum_direction(self, direction):
        return sum([int(i[1]) for i in self.instructions if i[0] == direction])

    def turn(self, direction, degrees):
        assert degrees in ('90', '180', '270'), \
            f'Wrong amount of degrees: {degrees}'
        assert direction in ('L', 'R'), \
            f'Unkown argument for direction: {direction}'
        if degrees == '180':
            self.direction *= -1
            return
        if degrees == '270':
            direction = {'L': 'R', 'R': 'L'}[direction]  # One turn in the other direction.
        if direction == 'R':
            self.direction = turn_right_transformation @ self.direction
        else:
            self.direction = turn_left_transformation @ self.direction

    def forward(self, distance):
        self.position += distance * self.direction

    def turn_and_forward(self):
        for i in self.instructions:
            if i[0] in ('N', 'E', 'S', 'W'):
                continue
            elif i[0] in ('L', 'R'):
                self.turn(*i)
            elif i[0] == 'F':
                self.forward(int(i[1]))
            else:
                raise ValueError('Unkown instruction.')

    def manhattan_d(self):
        return np.abs(self.position).sum()

    def task1(self):
        sum_north = self.sum_direction('N')
        sum_south = self.sum_direction('S')
        sum_east = self.sum_direction('E')
        sum_west = self.sum_direction('W')

        up_down = sum_north - sum_south
        left_right = sum_east - sum_west

        self.position += np.array((left_right, up_down))
        self.turn_and_forward()
        print(f"The answer is {self.manhattan_d()}.")


class day12_task2():

    def __init__(self):
        self.instructions = self.load_data()
        self.position = np.array((0, 0))
        self.waypoint = np.array((10, 1))

    def load_data(self):
        with open('./input.txt') as fp:
            txt = fp.read().splitlines()
        re_patt = r"^(\w)(\d+)$"
        return [re.match(re_patt, i).groups() for i in txt]

    def rotate(self, direction, degrees):
        assert degrees in ('90', '180', '270'), \
            f'Wrong amount of degrees: {degrees}'
        assert direction in ('L', 'R'), \
            f'Unkown argument for direction: {direction}'
        if degrees == '180':
            self.waypoint *= -1
            return
        if degrees == '270':
            direction = {'L': 'R', 'R': 'L'}[direction]  # One turn in the other direction.
        if direction == 'R':
            self.waypoint = turn_right_transformation @ self.waypoint
        else:
            self.waypoint = turn_left_transformation @ self.waypoint

    def forward(self, distance):
        self.position += distance * self.direction

    def manhattan_d(self):
        return np.abs(self.position).sum()

    def move_w(self, direction, distance):
        vector = np.array({'N': [0, 1], 'E': [1, 0],
                           'S': [0, -1], 'W': [-1, 0],
                           }[direction])
        self.waypoint += distance * vector

    def task2(self):
        for i in self.instructions:
            if i[0] in ('N', 'E', 'S', 'W'):
                self.move_w(i[0], int(i[1]))
            elif i[0] == 'F':
                self.position += int(i[1]) * self.waypoint
            else:
                self.rotate(*i)

        print(f"The answer is {self.manhattan_d()}.")


solver = day12_task1()

solver.task1()

solver2 = day12_task2()
solver2.task2()
