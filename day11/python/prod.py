class Monkey(object):
    def __init__(self, divisibly_by, multby, addto, square, ifTrue, ifFalse):
        self.divisible_by = divisibly_by
        self.multby = multby
        self.addto = addto
        self.square = square
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.items = []
        self.numOfInspections = 0

    def operation(self, x):
        if self.addto > 0:
            return x + self.addto
        elif self.multby != 1:
            return x * self.multby
        elif self.square:
            return x * x
        else:
            assert False

    def test(self, x):
        return x % self.divisible_by == 0

    def __str__(self):
        return 'Monkey: %s, %s, %s, %s' % (self.divisible_by, self.operation, self.ifTrue, self.ifFalse)

def partA(filename: str, rounds=20, worryDecrease=3) -> int:
    lines = getLines(filename)
    operation = None
    items = []
    ifTrue = None
    ifFalse = None
    multby = 1
    addto = 0
    square = False
    monkeys = []
    for l in lines:
        if l.startswith('Monkey'):
            continue
        elif l.startswith('  Starting items: '):
            items = l[len('  Starting items: '):].split(', ')
            items = list(map(int, items))
        elif l.startswith('  Operation: '):
            org_op = l
            op = l.split(': ')[-1]
            assert op.startswith('new = ')
            _, op, arg2 = op.split(' = ')[-1].split(' ')

            if op == '+':
                if arg2 == 'old':
                    multby = 2
                else:
                    addto = int(arg2)
            elif op == '*':
                if arg2 == 'old':
                    square = True
                else:
                    multby = int(arg2)
        elif l.startswith('  Test: '):
            divisibleBy = int(l.split(' ')[-1])
        elif l.startswith('    If true: '):
            ifTrue = int(l.split(' ')[-1])
        elif l.startswith('    If false: '):
            ifFalse = int(l.split(' ')[-1])
        elif l == '':
            m = Monkey(divisibleBy, multby, addto, square, ifTrue, ifFalse)
            m.org_op = org_op
            m.items = items
            monkeys += [m]
            items = []
            ifTrue = None
            ifFalse = None
            multby = 1
            addto = 0
            square = False

    import time
    global x
    x = time.time()

    def round(monkeys, modulo=1e9999):
        global x
        for m in range(len(monkeys)):
            monkey = monkeys[m]
            while monkey.items:
                monkey.numOfInspections += 1
                item = monkey.items.pop()
                item = monkey.operation(item)
                item //= worryDecrease
                item = item % modulo
                if monkey.test(item):
                    monkeys[monkey.ifTrue].items.append(item)
                else:
                    monkeys[monkey.ifFalse].items.append(item)

    m = 1
    for n in monkeys:
        m *= n.divisible_by

    for r in range(rounds):
        round(monkeys, modulo=m)

    ordered = sorted(monkeys, key=lambda x: x.numOfInspections)
    m1, m2 = ordered[-2:]
    return m1.numOfInspections * m2.numOfInspections

def partB(filename: str) -> int:
    lines = getLines(filename)
    return partA(filename, rounds=10000, worryDecrease=1)

def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.rstrip('\n')
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/sample.txt'))
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/sample.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))