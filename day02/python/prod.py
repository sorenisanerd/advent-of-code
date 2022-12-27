handScoreMap = dict()
handScoreMap['Rock'] = 1
handScoreMap['Paper'] = 2
handScoreMap['Scissors'] = 3
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

    score = 0
    for (them, me) in data:
        theirMove = theirMoveMap[them]
        myMove = myMoveMap[me]

        score += roundScore(theirMove, myMove)

    return score

valid_move = ['Rock', 'Paper', 'Scissors']

def roundScore(theirMove: str, myMove:str) -> int:
    assert theirMove in valid_move
    assert myMove in valid_move

    if theirMove == myMove:
        outcomeScore = 3 # Draw
    elif theirMove == 'Rock':
        outcomeScore = myMove == 'Paper' and 6 or 0
    elif theirMove == 'Paper':
        outcomeScore = myMove == 'Scissors' and 6 or 0
    else:
        outcomeScore = myMove == 'Rock' and 6 or 0

    handScore = handScoreMap[myMove]

    return outcomeScore + handScore

def partB(filename: str) -> int:
    data = getData(filename)
    theirMoveMap = dict()
    theirMoveMap['A'] = 'Rock'
    theirMoveMap['B'] = 'Paper'
    theirMoveMap['C'] = 'Scissors'

    # Given their move and our desired outcome (X -> Lose, Y -> Draw, Z -> Win)
    # calculate our move
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
        theirMove = theirMoveMap[them]
        myMove = myMoveMap[theirMove][outcome]
        score += roundScore(theirMove, myMove)

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