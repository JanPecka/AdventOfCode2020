"""Binary boarding"""

def load_data():
    with open('./input.txt') as fp:
        file = fp.read()
    return file.splitlines()


def get_seat_id(row, column):
    return row * 8 + column


def task1_binary(b_p):

    decoded = [(p
                .replace('F', '0')
                .replace('B', '1')
                .replace('R', '1')
                .replace('L', '0')
                )
               for p in b_p
               ]
    rows = [int(r[:7], 2) for r in decoded]
    cols = [int(c[7:], 2) for c in decoded]

    ids = map(lambda t: get_seat_id(*t), zip(rows, cols))

    # return max(ids)
    return set(ids)


def task2(ids):
    """316 µs ± 14.7 µs"""
    seats_w_neighbors = {i for i in set(range(min(ids), max(ids)))
                         if (i - 1) in ids
                         and (i + 1) in ids
                         }
    return seats_w_neighbors - ids


def task2_sets(ids):
    """90.2 µs ± 493 ns"""
    all_seats = set(range(min(ids), max(ids)))
    missing_seats = all_seats - ids
    return missing_seats


def task2_comprehension(ids):
    """73.7 µs ± 7.53 µs"""
    for i in ids:
        if (i + 1) not in ids:
            return (i + 1)


boarding_passes = load_data()

ids = task1_binary(boarding_passes)

print(task2(ids))
print(task2_sets(ids))