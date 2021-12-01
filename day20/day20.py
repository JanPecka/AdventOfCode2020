import numpy as np

IMG_SIZE = 10
GRID_SIZE = 12

class day20():

    def __init__(self):
        self.load_data()
        self.grid = np.zeros((2 * GRID_SIZE, 2 * GRID_SIZE))

    def load_data(self):
        with open('./input.txt') as fp:
            txt = fp.read().split('\n\n')

        self.images = {}
        for p in txt:
            p_nr = p.splitlines()[0][:-1].split( )[1]
            p_img = np.array([list(row.replace('#', '1').replace('.', '0'))
                              for row in p.splitlines()[1:]], dtype=int)
            self.images[p_nr] = p_img

    def extract_borders(self, img):
        return [img[0, :], img[:, -1], img[-1, :], img[:, 0]]

    def reverse_borders(self):  # Flips and rotations
        for pid, borders in self.borders.items():
            borders.extend([b[::-1] for b in borders])

    def align_borders(self, img_id, borders):
        for img2_id, borders2 in self.borders.items():
            if img_id == img2_id:
                continue
            if set(borders) - set(borders2):
                return img_id


    def task1(self):
        self.borders = {pid: self.extract_borders(img)
                        for pid, img in self.images.items()}
        self.reverse_borders()

        # Place the first in the center
        self.grid[GRID_SIZE, GRID_SIZE] = self.images.keys[0]
        for img_id, img_borders in self.borders.items():




solver = day20()

solver.task1()
