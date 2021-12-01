import numpy as np

class day10:  # Ways of connecting adapters

    def load_data(self):
        with open('./input.txt') as fp:
            return fp.read().splitlines()

    def parse_data(self):
        return [int(i) for i in self.adapters]

    def QA(self):
        assert len(self.adapters) == len(set(self.adapters)), 'Weird input!'

    def example1(self):
        self.adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.device_joltage = max(self.adapters) + 3
        self.task1_np()
        self.task2()

    def example2(self):
        self.adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
                         45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2,
                         34, 10, 3]
        self.device_joltage = max(self.adapters) + 3
        self.task1_np()
        print(self.task2())

    def __init__(self):
        self.adapters = self.load_data()
        self.adapters = self.parse_data()
        self.allowed_diference = range(1, 4)
        self.outlet_joltage = 0
        self.device_joltage = max(self.adapters) + 3

    def count_paths(self, bulk):
        length = len(bulk)
        for j in self.allowed_diference:
            if j < length:
                self.count_paths(bulk[j:])
            elif j == length:
                self.count += 1
            else:
                break

    def task1_np(self):
        adapters_in_order = np.sort(self.adapters)
        differences = np.diff(adapters_in_order,
                              prepend=self.outlet_joltage,
                              append=self.device_joltage,
                              )
        if set(differences[:-1]) - set(self.allowed_diference):
            print("Couldn't connect all the adapters")
        else:
            self.differences = differences
            self.task1_answer = np.unique(differences, return_counts=True)

    def task2(self):
        """It is enough to calculate the number of ways of moving between each
        pairs of two successive numbers different by 3."""
        values_among_threes = np.split(self.differences,
                                       np.where(self.differences == 3)[0],
                                       )
        options_per_bulk = []
        for bulk in values_among_threes:
            bulk = np.delete(bulk, np.where(bulk == 3))
            if len(bulk) > 0:
                self.count = 0
                self.count_paths(bulk)
                options_per_bulk.append(self.count)
        return np.array(options_per_bulk).astype(float).prod()


solver = day10()
solver.QA()

solver.task1_np()

print(solver.task2())
