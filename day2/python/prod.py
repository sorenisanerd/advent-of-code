def partA(filename: str) -> int:
    data = getData(filename)
    a = dict()
    a['A'] = 'Rock'
    a['B'] = 'Paper'
    a['C'] = 'Scissors'
    b = dict()
    b['X'] = 'Rock'
    b['Y'] = 'Paper'
    b['Z'] = 'Scissors'
    c = dict()
    c['Rock'] = 1
    c['Paper'] = 2
    c['Scissors'] = 3
    d = dict()
    d['Lose'] = 0
    d['Draw'] = 3
    d['Win'] = 6

    data = getData(filename)
    score = 0
    for (them, me) in data:
        winner = whoWins(a[them], b[me])
        e = dict()
        e[-1] = 'Lose'
        e[0] = 'Draw'
        e[1] = 'Win'

        score += d[e[winner]] + c[b[me]]

    return score

def whoWins(a: str, b:str) -> int:
    if a == b:
        return 0

    if a == 'Rock':
        return b == 'Paper' and 1 or -1
    if a == 'Paper':
        return b == 'Scissors' and 1 or -1
    # So it must be 'Scissors'
    return b == 'Rock' and 1 or -1

def partB(filename: str) -> int:
    data = getData(filename)
    a = dict()
    a['A'] = 'Rock'
    a['B'] = 'Paper'
    a['C'] = 'Scissors'
    b = dict()
    b['Rock'] = dict()
    b['Paper'] = dict()
    b['Scissors'] = dict()
    b['Rock']['X'] = 'Scissors'
    b['Rock']['Y'] = 'Rock'
    b['Rock']['Z'] = 'Paper'
    b['Paper']['X'] = 'Rock'
    b['Paper']['Y'] = 'Paper'
    b['Paper']['Z'] = 'Scissors'
    b['Scissors']['X'] = 'Paper'
    b['Scissors']['Y'] = 'Scissors'
    b['Scissors']['Z'] = 'Rock'
    c = dict()
    c['Rock'] = 1
    c['Paper'] = 2
    c['Scissors'] = 3
    d = dict()
    d['Lose'] = 0
    d['Draw'] = 3
    d['Win'] = 6

    data = getData(filename)
    score = 0
    for (them, outcome) in data:
        me = b[a[them]][outcome]

        e = dict()
        e['X'] = 'Lose'
        e['Y'] = 'Draw'
        e['Z'] = 'Win'
        score += d[e[outcome]] + c[me]

    return score



def getData(filename: str) -> list:
    rv = []
    with open(filename) as f:
        for l in f:
            l = l.strip()
            a, b = l.split(' ')
            rv += [(a, b)]
    return rv

if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))