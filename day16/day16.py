import re
import numpy as np

class day16():  # Parsing tickets based on rules for values

    def __init__(self):
        self.load_data()

    def load_data(self):

        def parse_rules(rules):
            ans = {}
            for r in rules.splitlines():
                re_m = re.match('^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)$', r).groups()
                ans[re_m[0]] =  [range(int(re_m[1]), int(re_m[2]) + 1),
                                 range(int(re_m[3]), int(re_m[4]) + 1)]
            return ans

        with open('./input.txt') as fp:
            rules, my_ticket, tickets = fp.read().split('\n\n')
        self.rules = parse_rules(rules)
        self.my_ticket = my_ticket.splitlines()[1].split(',')
        self.tickets = [[int(s) for s in l.split(',')]
                        for l in tickets.splitlines()[1:]]

    def collect_all_possible_values(self):
        vals = {x for ranges in self.rules.values() for r in ranges for x in r}
        return vals

    def keep_valid_tickets(self):
        all_poss_vals = self.collect_all_possible_values()
        self.valid_tickets = [t for t in self.tickets
                              if not set(t) - all_poss_vals]

    def collect_values_per_position(self):
        ticket_length = len(self.valid_tickets[0])
        vals_per_pos = [{t[i] for t in self.valid_tickets}
                        for i in  range(ticket_length)]
        return vals_per_pos

    def get_allowed_values(self):
        return {key: set(ranges[0]) | set(ranges[1])
                for key, ranges in self.rules.items()}

    def find_possible_positions(self, vals_per_p, allowed_vals):
        poss_pos = {}
        for key, allowed_vals in allowed_vals.items():
            poss_pos[key] = {
                i for i, all_vals in enumerate(vals_per_p)
                if not all_vals - allowed_vals  # No unallowed values.
                }
        return poss_pos

    def filter_possible_positions(self, poss_p):
        self.positions = {}

        while poss_p:

            found_keys = []

            for key, positions in poss_p.items():
                positions -= set(self.positions.values())
                if len(positions) > 1:
                    continue
                elif len(positions) == 1:
                    self.positions[key] = positions.pop()
                    found_keys.append(key)

            for k in found_keys:
                del poss_p[k]

        assert set(self.positions.keys()) == set(self.rules.keys()), \
            "Couldn't indentify all positions."

    def get_answer(self):
        ans = 1.
        for key, pos in self.positions.items():
            if 'departure' in key:
                ans *= float(self.my_ticket[pos])
        return ans

    def task1(self):
        ans = 0
        all_poss_vals = self.collect_all_possible_values()

        for ticket in self.tickets:
            extra_vals = set(ticket) - all_poss_vals
            ans += sum(extra_vals)

        print(f'The answer is {ans}.')

    def task2(self):
        self.keep_valid_tickets()
        values_per_position = self.collect_values_per_position()
        allowed_values = self.get_allowed_values()
        possible_positions = self.find_possible_positions(values_per_position,
                                                          allowed_values)
        self.filter_possible_positions(possible_positions)
        print(f'The answer is {self.get_answer()}.')


solver = day16()

solver.task2()
