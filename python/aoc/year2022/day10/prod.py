def partA(filename: str) -> int:
    lines = getLines(filename)
    history = calculateHistory(lines)

    counter = 0
    for x in range(19, len(history), 40):
        counter += (x+1)*history[x]

    return counter

def calculateHistory(lines):
    history = [1]
    for l in lines:
        args = l.split(' ')
        history += history[-1:]

        if args[0] == 'noop':
            continue

        _, val = l.split()
        history += [history[-1] + int(val)]
    return history

def partB(filename: str) -> int:
    lines = getLines(filename)
    history = calculateHistory(lines)

    for h in range(len(history)):
        sprite_position = history[h]
        col = h % 40
        if abs(col-sprite_position) < 2:
            history[h] = '#'
        else:
            history[h] = '.'

    rv = []
    for i in range(0, 240, 40):
        rv += [''.join(history[i:i+40])]

    return '\n'.join(rv)

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
