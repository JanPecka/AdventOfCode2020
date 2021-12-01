def load_data():
    with open('./input.txt') as fp:
        file = fp.read()
    return file.split('\n\n')


def task1_map(groups):
    """1.05 ms ± 71.6 µs"""
    nr_pos_questions = map(
        lambda s: len(set(s.replace('\n', ''))),
        groups,
        )
    return sum(nr_pos_questions)


def task1_map2(groups):
    """1.24 ms ± 22 µs"""
    nr_pos_questions = map(
        lambda s: len(set(s) - {'\n'}),
        groups,
        )
    return sum(nr_pos_questions)


def task1_comprehension(groups):
    nr_pos_questions = [len(set(s.replace('\n', ''))) for s in groups]
    return sum(nr_pos_questions)


def task2_set(groups):
    common_count = 0
    for g in groups:
        persons = g.splitlines()
        answers_per_person = [set(p) for p in persons]
        common_answers = set.intersection(*answers_per_person)
        common_count += len(common_answers)
    return common_count


groups = load_data()

print(task1_map(groups))
print(task1_comprehension(groups))
print(task1_map2(groups))

print(task2_set(groups))