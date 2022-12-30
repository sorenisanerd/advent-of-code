def partA(filename: str) -> int:
    lines = getLines(filename)
    rv = 0
    for l in lines:
        rv += snafuToDecimal(l)

    return decimalToSnafu(rv)

def decimalToSnafu(num):
    rv = ''

    if num == 0:
        return '0'

    while num>0:
        digit = int(num%5)
        if digit == 4:
            rv += '-'
            num += 5
        elif digit == 3:
            rv += '='
            num += 5
        else:
            rv += str(digit)
        num //= 5
    return rv[::-1]

#   Decimal          SNAFU
#         1              1
#         1              =
#         1              -

#         0              0
#         1              1
#         2              2
#         3             1=
#         4             1-
#         5             10
#         6             11
#         7             12
#         8             2=
#         9             2-
#        10             20
#        11             21
#        12             22
#        13            1==
#        14            1=-
#        15            1=0
#        16            1=1
#        17            1=2
#        18            1-=
#        19            1=-
#        20            1-0
#        21            1-1
#        22            1-2
#        23            10=
#        24            10-
#        25            100
#        26            101
#        20            102
#      2022         1=11-2
#     12345        1-0---0
def decimalTasdfasdfoSnafu(decimal: int) -> str:
    s = dec_to_base(decimal, 5)
    rv = ''
    for c in s:
        if c == '1':
            rv += '1'
        elif c == '2':
            rv += '2'
        elif c == '0':
            rv += '1-'
        elif c == '3':
            rv += '1-'
            assert False
# 112 04  11044030
# 112 1-1 110 -1=0

def snafuToDecimal(snafu: str) -> int:
    rv = 0
    length = len(snafu)
    for i, c in enumerate(snafu):
        if c in '012':
            v = int(c)
        elif c == '=':
            v = -2
        elif c == '-':
            v = -1
        else:
            assert False

        rv += v * 5 ** (length - i - 1)
    return rv


def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.rstrip('\n')
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
