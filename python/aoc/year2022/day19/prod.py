import re

def addVectors(v1, v2):
    return tuple((len(v1) >= i+1 and v1[i] or 0) +
                 (len(v2) >= i+1 and v2[i] or 0) for i in range(max(len(v1), len(v2))))

def multiplyVectorByScalar(v, x):
    return tuple(v_*x for v_ in v)

def invertVector(v):
    return tuple(-x for x in v)

def solve(blueprint, time_left=24):
    if time_left == 0:
        print('ran out of time')
        return 0

    d = dict()
    d['ans'] = -1

    # order: (0:ore, 1:clay, 2:obsidian, 3:geode)
    def dfs(resources, robots, time_left, d=d):
        # what the heck is going on?
        assert min(resources) >= 0
        assert min(robots) >= 0

        # Base case is just hanging out, letting the geode robots do their thing
        whatIfWeJustHangOut = resources[3] + robots[3] * time_left

        if whatIfWeJustHangOut > d['ans']:
            d['ans'] = whatIfWeJustHangOut

        # If we had enough resources to generate a new geode robot every
        # minute until we ran out of time, we'd generate an additional
        # 1 geode next minute, an additional 2 the minute after that,
        # 3 the minute after that, etc.
        # 1+2+3+....+n = n*(n+1)//2
        if d['ans'] > whatIfWeJustHangOut + (time_left)*(time_left-1)//2:
            return

        def turnsNeeded(robotCost, resources=resources, robots=robots):
            turns = []
            for res, robot, cost in zip(resources, robots, robotCost):
                if res >= cost:
                    turns += [0]
                elif robot:
                    # c-r is cost - resources, so how many we're short
                    # We'll generate b of them this turn, though, so we add
                    # that back.
                    turns += [(robot + cost - res - 1) // robot]
                else:
                    # We don't have any robots generating this kind of resource
                    # so any number of turns won't help us.
                    return 10000

            return max(turns)

        # blueprint = (0:bpid, 1:ore_robot_cost, 2:clay_robot_cost,
        # 3:obsidian_robot_ore_cost, 4:obsidian_robot_clay_cost,
        # 5:geode_robot_ore_cost, 6:geode_robot_obsidian_cost)
        costs = [
            # Geode robots
            [3, (blueprint[5], 0, blueprint[6], 0)],
            # Obsidian robots
            [2, (blueprint[3], blueprint[4], 0, 0)],
            # Clay robots
            [1, (blueprint[2], 0, 0, 0)],
            # Ore robots
            [0, (blueprint[1], 0, 0, 0)],
        ];

        # order: (0:ore, 1:clay, 2:obsidian, 3:geode)
        for (i, robotCost) in costs:
            if i < 3:
                # robots[i] is how many robots are generating this resource.
                # if that's more than any of the robots cost, there's no
                # point building more of them. i == 3 is geodes, though, and
                # we don't want to restrict how many we make of those, duh.
                if (robots[i] >= max(c[1][i] for c in costs)):
                    continue

            t = turnsNeeded(robotCost)

            if (t < time_left):
                new_robots = list(robots)
                new_robots[i] += 1

                # Existing robots keep doing their thing
                res_ = multiplyVectorByScalar(robots, t+1)

                # Add what we had when we started
                res_ = addVectors(res_, resources)

                # Subtract what this robot costs to make
                res_ = addVectors(res_, invertVector(robotCost))

                dfs(res_, tuple(new_robots), time_left-t-1)

    dfs((0, 0, 0, 0), (1, 0, 0, 0), time_left)
    return d['ans']

def partA(filename: str) -> int:
    lines = getLines(filename)
    blueprints = parseBlueprints(lines)

    rv = 0
    for blueprint in blueprints:
        rv += blueprint[0]*solve(blueprint, 24)

    return rv

def parseBlueprints(lines):
    reg = re.compile('Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')

    blueprints = []
    for l in lines:
        match = reg.match(l)
        assert match

        blueprints += [tuple(map(int, match.groups()))]
    return blueprints

def partB(filename: str) -> int:
    lines = getLines(filename)
    blueprints = parseBlueprints(lines)

    rv = 1
    for blueprint in blueprints[:3]:
        rv *= solve(blueprint, 32)

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
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))
