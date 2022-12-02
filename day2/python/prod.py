handScore = dict()
handScore['Rock'] = 1
handScore['Paper'] = 2
handScore['Scissors'] = 3
outcomeScore = dict()
outcomeScore['Lose'] = 0
outcomeScore['Draw'] = 3
outcomeScore['Win'] = 6

def partA(filename: str) -> int:
    data = getData(filename)
    theirMoveMap = dict()
    theirMoveMap['A'] = 'Rock'
    theirMoveMap['B'] = 'Paper'
    theirMoveMap['C'] = 'Scissors'
    myMoveMap = dict()
    myMoveMap['X'] = 'Rock'
    myMoveMap['Y'] = 'Paper'
    myMoveMap['Z'] = 'Scissors'

    data = getData(filename)
    score = 0
    for (them, me) in data:
        theirMove = theirMoveMap[them]
        myMove = myMoveMap[me]
        # print('They play %s, so I play %s' % (theirMove, myMove))

        winner = whoWins(theirMove, myMove)
        outcomeMap = dict()
        outcomeMap[-1] = 'Lose'
        outcomeMap[0] = 'Draw'
        outcomeMap[1] = 'Win'

        # print('I %s' % (outcomeMap[winner]))
        score += outcomeScore[outcomeMap[winner]] + handScore[myMoveMap[me]]

    return score

def whoWins(a: str, b:str) -> int:
    if a == b:
        return 0

    if a == 'Rock':
        return b == 'Paper' and 1 or -1
    if a == 'Paper':
        return b == 'Scissors' and 1 or -1

    # So a must be 'Scissors'
    return b == 'Rock' and 1 or -1

def partB(filename: str) -> int:
    data = getData(filename)
    theirMoveMap = dict()
    theirMoveMap['A'] = 'Rock'
    theirMoveMap['B'] = 'Paper'
    theirMoveMap['C'] = 'Scissors'
    myMoveMap = dict()
    myMoveMap['Rock'] = dict()
    myMoveMap['Paper'] = dict()
    myMoveMap['Scissors'] = dict()
    myMoveMap['Rock']['X'] = 'Scissors'
    myMoveMap['Rock']['Y'] = 'Rock'
    myMoveMap['Rock']['Z'] = 'Paper'
    myMoveMap['Paper']['X'] = 'Rock'
    myMoveMap['Paper']['Y'] = 'Paper'
    myMoveMap['Paper']['Z'] = 'Scissors'
    myMoveMap['Scissors']['X'] = 'Paper'
    myMoveMap['Scissors']['Y'] = 'Scissors'
    myMoveMap['Scissors']['Z'] = 'Rock'

    data = getData(filename)
    score = 0
    for (them, outcome) in data:
        me = myMoveMap[theirMoveMap[them]][outcome]

        e = dict()
        e['X'] = 'Lose'
        e['Y'] = 'Draw'
        e['Z'] = 'Win'
        score += outcomeScore[e[outcome]] + handScore[me]

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