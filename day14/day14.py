import re
import numpy as np

NR_BITS = 36

re_patt_mem = r"^mem\[(\d+)\] = (\d+)$"

class day14():  # Bitmasks

    def __init__(self):
        self.codes = self.load_data()
        self.memory = {}

    def load_data(self):
        with open('./input.txt') as fp:
            return fp.read().splitlines()

    def parse_mem_line(self, s):
        i_val = re.match(re_patt_mem, s).groups()
        return (int(i) for i in i_val)

    def apply_mask(self, mask, value):
        value_bin = np.array(list(bin(value)[2:].zfill(len(mask))))
        masked = np.where(mask == 'X', value_bin, mask)
        return int(''.join(masked), 2)

    def apply_mask_with_floating(self, mask, address):
        address_bin = np.array(list(bin(address)[2:].zfill(len(mask))))
        masked = np.where(mask == '0', address_bin, mask)
        return ''.join(masked)

    def fill_memory(self, address, val):
        while 'X' in address:
            for i in (0, 1):
                address_x_replaced = address.replace('X', str(i), 1)
                self.fill_memory(address_x_replaced, val)
            break
        else:
            self.memory[int(address, 2)] = val

    def task1(self):
        for line in self.codes:
            if 'mask' in line:
                mask = np.array(list(line.split(' = ')[1]))
            elif 'mem' in line:
                index, value = self.parse_mem_line(line)
                transformed = self.apply_mask(mask, value)
                self.memory[index] = transformed
            else:
                raise ValueError('Unkown type of instruction!')
        print(f'The answer is {sum(self.memory.values())}.')

    def task2(self):
        for line in self.codes:
            if 'mask' in line:
                mask = np.array(list(line.split(' = ')[1]))
            elif 'mem' in line:
                index, value = self.parse_mem_line(line)
                transformed_i = self.apply_mask_with_floating(mask, index)
                self.fill_memory(transformed_i, value)
        print(f'The answer is {sum(self.memory.values())}.')



solver = day14()

# solver.task1()

solver.task2()

