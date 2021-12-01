import numpy as np

ACTIVE = '#'
INACTIVE = '.'

# Possible improvements:
# - the game is symmetric, you could only calculate one side of the cube
# - if there is an empty outer-most layer after a cycle, remove it

class day17():  # Game of life in n dimensions.

    def __init__(self, n_dims):
        self.starting_arr = self.load_data()
        self.dimension = n_dims
        self.n_activate = {3}
        self.n_deactivate = {2, 3}

    def load_data(self):
        with open('./input.txt') as fp:
            return np.array([list(l.replace(ACTIVE, '1').replace(INACTIVE, '0'))
                             for l in fp.read().splitlines()], dtype=int)

    def get_area(self, arr, index):
        slices = [slice(max(i - 1, 0), min(i + 2, arr.shape[dim]))
                  for dim, i in enumerate(index)]
        area = arr[slices]
        return area

    def change_state(self, curr_state, n_neighbors):
        if curr_state == 1 and n_neighbors not in self.n_deactivate:
            state = 0
        elif curr_state == 0 and n_neighbors in self.n_activate:
            state = 1
        else:
            state = curr_state
        return state

    def one_cycle(self):
        arr = self.current_arr
        arr = np.pad(arr, 1, mode='constant', constant_values=0)
        next_arr = np.zeros(arr.shape, dtype=int)

        it = np.nditer(arr, flags=['multi_index'])
        for x in it:
            area = self.get_area(arr, it.multi_index)
            active_neighbors = np.sum(area) - x
            next_arr[it.multi_index] = self.change_state(x, active_neighbors)
        self.current_arr = next_arr

    def game_of_life(self):
        self.current_arr = np.resize(
            self.starting_arr,
            [*self.starting_arr.shape] + [1] * (self.dimension
                                                - len(self.starting_arr.shape)
                                                )
            )

        for i_cycle in range(6):
            self.one_cycle()

        print(f"The answer is {np.sum(self.current_arr)}.")


solver = day17(4)

solver.game_of_life()
