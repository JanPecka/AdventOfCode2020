import re

class day19():  # Regex recursion

    def __init__(self):
        self.load_data()
        self.parse_data()
        self.re_patts = {}

    def load_data(self):
        with open('./input.txt.') as fp:
            txt = fp.read()
            self.rules, self.messages = txt.split('\n\n')

    def parse_data(self):
        # Rules.
        rules = {}
        for r in self.rules.splitlines():
            key = r.split(':')[0]
            r = r.replace(f'{key}: ', '')
            if "\"" in r:
                val = re.search(r"\"(\w+)\"", r).group(1)
            else:
                val = [tuple(s.strip().split(' ')) for s in r.split('|')]
            rules[key] = val
        self.rules = rules

        # Messages
        self.messages = self.messages.splitlines()

    def create_regex(self, rule_nr):
        if rule_nr in self.re_patts:
            return self.re_patts[rule_nr]
        rule = self.rules[rule_nr]

        if type(rule) ==     str:
            return rule
        elif type(rule) == list:
            if len(rule) > 1:
                patt = '(' + '|'.join([
                    ''.join([self.create_regex(r) for r in pipe])
                    for pipe in rule
                    ]) + ')'
            else:
                patt = ''.join([self.create_regex(r) for r in rule[0]])
            self.re_patts[rule_nr] = patt
            return patt

    def modify_rule_8(self):
        rule8 = self.rules['8']
        rule8_atom = ['42']
        for recursion in range(2, 21):
            rule8.append(tuple(rule8_atom * recursion))
        self.rules['8'] = rule8

    def modify_rule_11(self):
        rule11 = self.rules['11']
        rule11_atom = ['42', '31']
        rule11_pre = '42'
        rule11_post = '31'
        for recursion in range(1, 21):
            rule11.append(tuple(([rule11_pre] * recursion
                                 + rule11_atom
                                 + [rule11_post] * recursion
                                 )))
        self.rules['11'] = rule11

    def task1(self):
        re_patt = self.create_regex('0')
        count = 0

        for m in self.messages:
            if re.fullmatch(re_patt, m):
                count += 1

        print(f'The answer is {count}.')

    def task2(self):
        self.modify_rule_8()
        self.modify_rule_11()

        re_patt = self.create_regex('0')
        count = 0

        for m in self.messages:
            if re.fullmatch(re_patt, m):
                count += 1

        print(f'The answer is {count}.')


solver = day19()

solver.task2()
