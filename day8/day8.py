import re
import anytree as at
import igraph as ig

"""Switch one instruction to reach the goal."""

def load_data():
    with open('./input.txt') as fp:
        file = fp.read()
    return file.splitlines()


def parse_line(s):
    re_patt = r"(\w{3}) ([+-])(\d+)$"
    action, sign, amount = re.match(re_patt, s).groups()
    signed_amount = int(amount) if sign == '+' else -int(amount)
    return action, signed_amount


def action(row, acc, index):
    if row[0] == 'acc':
        acc += row[1]
        index += 1
    elif row[0] == 'jmp':
        index += row[1]
    else:
        index += 1
    return acc, index


def graph(instructions):
    g = ig.Graph()
    g.add_vertices(len(instructions) + 1)
    g.vs['label'] = [str(i) for i in range(0, len(instructions))] + ['END']

    edges = []
    for index, row in enumerate(instructions):
        row = parse_line(row)
        _, next_index = action(row, 0, index)
        edges.append((index, next_index))

    g.add_edges(edges)
    # g.write_svg('./graph.svg', font_size=13,
                # edge_stroke_widths='width')
    # ig.plot(g, layout='auto').show()

    return g


def find_states_leading_to_finish(instructions):
    finish_state = {len(instructions)}  # End of file.

    for index, instruction in enumerate(reversed(instructions)):

        current_index = len(instructions) - index - 1

        _, next_index = action(parse_line(instruction), 0, current_index)

        if next_index in finish_state:  # Any path leading here also leads to victory.
            finish_state.add(current_index)

    return finish_state


def switch_one(instructions, winning_states):

    def switch_to_victory(row, index):

        if row[0] == 'jmp':
            _, next_index = action(['nop', row[1]], 0, index)
            if next_index in winning_states:
                return True

        elif row[0] == 'nop':
            _, next_index = action(['jmp', row[1]], 0, index)
            if next_index in winning_states:
                return True

        return False


    index = 0
    visited_indexes = set()
    acc = 0
    switch_flag = True

    while (index not in visited_indexes
           and index != len(instructions)):

        visited_indexes.add(index)
        row = parse_line(instructions[index])

        if row[0] in ('jmp', 'nop'):

            if switch_flag:
                if switch_to_victory(row, index):
                    acc, index = action(({'jmp': 'nop', 'nop': 'jmp'}[row[0]],
                                         row[1]
                                         ),
                                        acc,
                                        index
                                        )
                    switch_flag = False
                    continue

        acc, index = action(row, acc, index)

    if index == len(instructions):
        print('REACHED THE FINISH LINE')
        return acc
    else:
        print('NOPE')
        return acc


def stop_when_loop(instructions):
    index = 0
    visited_indexes = set()
    acc = 0

    while index not in visited_indexes:

        visited_indexes.add(index)
        row = parse_line(instructions[index])
        acc, index = action(row, acc, index)

    return acc


instructions = load_data()

# Task 1.
print(stop_when_loop(instructions))

# Task 2.
winning_states = find_states_leading_to_finish(instructions)
print(switch_one(instructions, winning_states))

g = graph(instructions)
ccc = g.components()
winning_states_2 = ccc.membership
winning_states_3 = [i for i, v in enumerate(winning_states_2) if v == 1]

print(switch_one(instructions, winning_states_3))

