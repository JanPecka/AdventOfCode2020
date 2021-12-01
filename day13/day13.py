import numpy as np

class day13():  # Chinese remainder theorem

    def __init__(self):
        self.load_data()
        self.get_difference()

    def load_data(self):
        with open('./input.txt') as fp:
            txt = fp.read().splitlines()
        self.arrival_time = int(txt[0])
        self.buses = np.array(txt[1].split(','))

    def test_example(self):
        self.buses = np.array('1789,37,47,1889'.split(','))
        self.get_difference()
        self.task2()

    def get_difference(self):
        buses = self.buses
        diffs_among_buses = np.split(buses, np.where(buses != 'x')[0][1:])
        self.differences = [len(diff) for diff in diffs_among_buses[:-1]]

    def task1(self):
        buses = np.delete(self.buses, np.where(self.buses == 'x')).astype(int)
        waiting_times = (np.ceil(self.arrival_time / buses) * buses
                         - self.arrival_time
                         )
        argmin = np.argmin(waiting_times)
        print(f"The answer is {buses[argmin] * waiting_times[argmin]}.")

    def find_interval(self, d1, d2, diff, init_time=0):
        """Find first possible `k` and `l` that satisfy the division equations."""
        d1_times = (d1 * float(i) + init_time for i in range(100000))
        first_occurence = None

        for time in d1_times:
            if (time + diff) % d2 == 0:
                if first_occurence is None:
                    first_occurence = time
                else:
                    second_occurence = time
                    break
        else:
            raise TimeoutError('Not enough iterations to find the interval.')

        return first_occurence, second_occurence


    def task2(self):
        buses = np.delete(self.buses, np.where(self.buses == 'x')).astype(int)
        differences_against_1 = np.cumsum(self.differences)
        time1 = buses[0]
        time0 = 0

        for bus, diff in zip(buses[1:], differences_against_1):
            time0, time1 = self.find_interval(time1 - time0, bus, diff, time0)

        print('Solution reached!')
        print(f'Answer: {time0}.')


solver = day13()

solver.task1()

solver.task2()
