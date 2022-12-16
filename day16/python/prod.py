import re

rega = re.compile('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')

# Takes a list and returns a generator returning
# 2-tuples like so:
# choose_one([1,2,3]):
# (1, [2,3])
# (2, [1,3])
# (3, [1,2])
# So first element of the tuple iterates over the list
# and the second element is the list without the first element
def choose_one(l):
    for i in range(len(l)):
        yield (l[i], l[:i] + l[i+1:])

def floyd_warshall(V):
    # Initialize the distance matrix
    dist = dict()
    for k in V.keys():
        dist[k] = dict()
        for k2 in V.keys():
            if k == k2:
                dist[k][k2] = 0
            else:
                dist[k][k2] = float('inf')

    # Add neigbors
    for k in V.keys():
        for t in V[k][1]:
            dist[k][t] = 1

    for k in V.keys():
        for i in V.keys():
            for j in V.keys():
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

cache1 = dict()
def dfs(V, distances, cur, rest, time_remaining=30):
    key = (cur, tuple(rest), time_remaining)
    if key not in cache1:
        cache1[key] = dfs_(V, distances, cur, rest, time_remaining)
    return cache1[key]

def dfs_(V, distances, cur, rest, time_remaining=30):
    if time_remaining == 0:
        return 0

    rv = 0
    for (next, new_rest) in choose_one(rest):
        if next is None:
            continue
        if distances[cur][next] < time_remaining:
            contribution = V[next][0] * (time_remaining - distances[cur][next] - 1)
            rv = max(rv, contribution + dfs(V, distances, next, new_rest, time_remaining - distances[cur][next] - 1))

    return rv

cache2 = dict()
def dfs2(V, distances, cur, rest, time_remaining=30):
    key = (cur, tuple(rest), time_remaining)
    if key not in cache2:
        cache2[key] = dfs2_(V, distances, cur, rest, time_remaining)
    return cache2[key]

def dfs2_(V, distances, cur, rest, time_remaining=26):
    if time_remaining == 0:
        return dfs(V, distances, 'AA', rest, 26)

    # We've been everywhere
    if not rest:
        return 0

    # Base case is having the elephant do the whole thing
    rv = dfs(V, distances, 'AA', rest, 26)

    for (next, new_rest) in choose_one(rest):
        if distances[cur][next] < time_remaining:
            contribution = V[next][0] * (time_remaining - distances[cur][next] - 1)
            rv = max(rv, contribution + dfs2(V, distances, next, new_rest, time_remaining - distances[cur][next] - 1))

    return rv


def partA(filename: str, start_time=30) -> int:
    lines = getLines(filename)

    V = dict()
    for l in lines:
        match = rega.match(l)
        if match is None:
            print(l)

        groups = match.groups()
        name, rate, tunnels = groups
        V[name] = (int(rate), tunnels.split(', '))

    distances = floyd_warshall(V)
    return dfs(V, distances, 'AA', list(filter(lambda v:V[v][0] > 0, V.keys())), start_time)


def partB(filename: str) -> int:
    lines = getLines(filename)

    V = dict()
    for l in lines:
        match = rega.match(l)
        if match is None:
            assert False

        groups = match.groups()
        name, rate, tunnels = groups
        V[name] = (int(rate), tunnels.split(', '))

    distances = floyd_warshall(V)
    return dfs2(V, distances, 'AA', list(filter(lambda v:V[v][0] > 0, V.keys())), 26)

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