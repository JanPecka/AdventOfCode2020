import re
import numpy as np
import anytree as at
from collections import deque

"""Tree of bags."""


def load_data():
    with open('./input.txt') as fp:
        file = fp.read()
    return file.splitlines()


def task1(rules, specified_color):

    def parse(rules):

        re_patt = r"(\d |)(\w+ \w+) bag"
        rule_map = {}

        for r in rules:

            groups = re.findall(re_patt, r)
            rule_map[groups[0][1]] = {t[1] for t in groups[1:]}

        return rule_map

    rule_map = parse(rules)
    specified_colors = {specified_color}
    specified_colors_old = set()
    res = set()

    while specified_colors != specified_colors_old:

        specified_colors_old = {c for c in specified_colors}

        for color, allowed_colors in rule_map.items():

            if len(specified_colors & allowed_colors) != 0:

                specified_colors.add(color)
                res.add(color)

    return res


def parse(rules):

    re_patt = r"(\d |)(\w+ \w+) bag"
    rule_map = {}

    for r in rules:

        groups = re.findall(re_patt, r)
        rule_map[groups[0][1]] = [g for g in groups[1:] if g[1] != 'no other']

    return rule_map


def task2(rules, specified_color):

    def parse(rules):

        re_patt = r"(\d |)(\w+ \w+) bag"
        rule_map = {}

        for r in rules:

            groups = re.findall(re_patt, r)
            rule_map[groups[0][1]] = [g for g in groups[1:]]

        return rule_map


    def count_color(c):

        count = 1
        bags_inside = rule_map[c]

        for count_inside, color_inside in bags_inside:

            if color_inside == 'no other':
                continue

            count += int(count_inside) * count_color(color_inside)

        return count

    rule_map = parse(rules)
    count = count_color(specified_color)

    return count


rules = load_data()
color = 'shiny gold'

# rules = """shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.""".split('\n')

# print(len(task1(rules, 'shiny gold')))
# print(task2(rules, 'shiny gold'))


def iterate(rule_map, color, node):
    for count_in, color_in in rule_map[color]:
        node = at.Node(color_in, parent=node, count=count_in)
        iterate(rule_map, color_in, node)


rule_map = parse(rules)
base = at.Node(color, count = 1)
iterate(rule_map, color, base)

for pre, fill, node in at.RenderTree(base):
    print("%s%s %s" % (pre, node.count, node.name))


