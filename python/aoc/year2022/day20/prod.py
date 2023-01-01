def shift(current_order, elem):
    curidx = current_order.index(elem)
    newidx = (curidx + elem[1]) % (len(current_order)-1)

    # If we're going backwards, we can't land on index 0,
    # but rather end at the end
    if newidx == 0:
        if elem[1] < 0:
            newidx = len(current_order)-1

    new_order = list(current_order)
    new_order.pop(curidx)
    new_order.insert(newidx, elem)
    return new_order

def partA(filename: str) -> int:
    return doStuff(filename)

def doStuff(filename: str, multiplier=1, rounds=1) -> int:
    lines = getLines(filename)
    original_order = [int(x)*multiplier for x in lines]
    current_order = list(enumerate(original_order))

    for _ in range(rounds):
        for elem in enumerate(original_order):
            current_order = shift(current_order, elem)

    for idx in range(len(current_order)):
        if current_order[idx][1] == 0:
            break

    return sum(current_order[(idx+idx_) % len(current_order)][1] for idx_ in [1000,2000,3000])

def partB(filename: str) -> int:
    return doStuff(filename, multiplier=811589153, rounds=10)

def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.rstrip('\n')
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(get_data_file_path('input.txt')))
    print(partB(get_data_file_path('input.txt')))
