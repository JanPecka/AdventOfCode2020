import numpy as np

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

class day11():  # Occupying seats

    def __init__(self):
        self.initial_state = self.load_data()
        self.height, self.width = self.initial_state.shape
        self.initial_state = self.add_padding(self.initial_state)
        self.nr_to_occ = 0
        self.nr_to_leave = 4

    def load_data(self):
        with open('./input.txt') as fp:
            txt = fp.read().splitlines()
            return np.array([list(s) for s in txt])

    def add_padding(self, state):
        """Add 'floor' around the map as dummy states."""
        return np.vstack((np.full((1, self.width + 2), FLOOR),
                          np.hstack((np.full((self.height, 1), FLOOR),
                                     state,
                                     np.full((self.height, 1), FLOOR)
                                     )),
                          np.full((1, self.width + 2), FLOOR),
                          ))

    def get_neighbours(self, state, i, j):
        assert i < self.height and j < self.width, 'Wrong indices for neighbors.'
        i, j = i + 1, j + 1  # To counteract the padding
        area = np.copy(state[(i - 1):(i + 2),
                             (j - 1):(j + 2)
                             ]
                       )
        area[1, 1] = FLOOR  # Dummy state, does not influence anything.
        return area

    def count_occupied(self, area):
        return np.char.count(area, OCCUPIED).sum().sum()

    def one_round_task1(self, state):
        next_state = np.copy(state)

        for i in range(self.height):
            for j in range(self.width):
                place = state[i + 1, j + 1]
                if place == FLOOR:
                    continue
                else:
                    neighbours = self.get_neighbours(state, i, j)
                    occupied_neighbours = self.count_occupied(neighbours)
                    if (place == EMPTY
                        and occupied_neighbours == self.nr_to_occ
                          ):
                        next_state[i + 1, j + 1] = OCCUPIED
                    elif (place == OCCUPIED
                          and occupied_neighbours >= self.nr_to_leave
                          ):
                        next_state[i + 1, j + 1] = EMPTY

        return next_state

    def look_in_dir(self, direction, state, index):
        index = np.array(index)
        while (all(index + direction >= 0)
               and all(index + direction < (self.height, self.width))
               ):
            index += direction
            if state[tuple(index)] == FLOOR:
                continue
            elif state[tuple(index)] == EMPTY:
                return 0
            elif state[tuple(index)] == OCCUPIED:
                return 1
        else:
            return 0

    def look_around(self, state, index):
        occupied_seats = 0
        for direction in [(-1, 0), (-1, 1), (0, 1), (1, 1),
                          (1, 0), (1, -1), (0, -1), (-1, -1)
                          ]:
            occupied_seats += self.look_in_dir(direction, state, index)
        return occupied_seats

    def one_round_task2(self, state):
        next_state = np.copy(state)

        for i in range(self.height):
            for j in range(self.width):
                place = state[i, j]
                if place == FLOOR:
                    continue
                else:
                    occupied_seats_in_view = self.look_around(state, (i, j))
                    if (place == EMPTY
                        and occupied_seats_in_view == self.nr_to_occ
                          ):
                        next_state[i, j] = OCCUPIED
                    elif (place == OCCUPIED
                          and occupied_seats_in_view >= self.nr_to_leave
                          ):
                        next_state[i, j] = EMPTY

        return next_state

    def task2(self):
        current_state = self.initial_state[1:-1, 1:-1]  # Padding not needed.
        self.nr_to_leave = 5  # Change in rules.

        for i in range(200):
            print(i)
            next_state = self.one_round_task2(current_state)
            if np.array_equal(current_state, next_state):
                print('Final state reached!')
                print(self.count_occupied(current_state))
                break
            current_state = next_state
        else:
            print('Not enough iterations.')

    def task1(self):
        current_state = self.initial_state
        for _ in range(100):  # Max nr. of iterations.
            next_state = self.one_round_task1(current_state)
            if np.array_equal(current_state, next_state):
                print('Final state reached!')
                print(self.count_occupied(current_state))
                break
            current_state = next_state
        else:
            print('Not enough iterations.')



solver = day11()

# solver.task1()

solver.task2()