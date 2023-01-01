def partA(filename: str) -> int:
    lines = getLines(filename)
    count = 0
    for l in lines:
        e1, e2 = l.split(',')
        e1start, e1end, e2start, e2end = map(lambda x:int(x), e1.split('-') + e2.split('-'))
        e1span = set(range(e1start, e1end+1))
        e2span = set(range(e2start, e2end+1))
        if e1span.issubset(e2span) or e2span.issubset(e1span):
            count += 1
    return count

def partB(filename: str) -> int:
    lines = getLines(filename)
    count = 0
    for l in lines:
        e1, e2 = l.split(',')
        e1start, e1end, e2start, e2end = map(lambda x:int(x), e1.split('-') + e2.split('-'))
        e1span = set(range(e1start, e1end+1))
        e2span = set(range(e2start, e2end+1))
        if e1span.intersection(e2span):
            count += 1
    return count

def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.strip()
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(get_data_file_path('input.txt')))
    print(partB(get_data_file_path('input.txt')))