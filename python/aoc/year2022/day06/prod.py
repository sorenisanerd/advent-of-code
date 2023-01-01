def partA(filename: str) -> int:
    lines = getLines(filename)
    l = lines[0]
    for i in range(0, len(l)-3):
        if len(set(l[i:i+4])) == 4:
            return i+4
    return -1

def partB(filename: str) -> int:
    lines = getLines(filename)
    l = lines[0]
    for i in range(0, len(l)-13):
        if len(set(l[i:i+14])) == 14:
            return i+14
    return -1

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