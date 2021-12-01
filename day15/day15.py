class day15():  # Van Eck's sequence

    def __init__(self):
        self.starting_sequence = [0, 1, 5, 10, 3, 12, 19]
        self.memory = {}  # Storing last occurences.

    def load_into_memory(self, seq, occ):
        for val, i in zip(seq, occ):
            self.memory[val] = i

    def task1(self):
        self.load_into_memory(self.starting_sequence[:-1],
                              range(0, len(self.starting_sequence) - 1)
                              )
        last_nr = self.starting_sequence[-1]

        for i in range(len(self.starting_sequence) - 1, 29999999):
            last_occ = self.memory.get(last_nr, i)
            self.memory[last_nr] = i
            last_nr = i - last_occ

        print(f"The answer is {last_nr}.")


solver = day15()

solver.task1()