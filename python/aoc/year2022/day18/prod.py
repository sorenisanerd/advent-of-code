def partA(filename: str) -> int:
    lines = getLines(filename)

    # all_surfaces contain 4-tuples of droplet surfaces:
    # x, y, z, d where x, y, z are coordinates of a block
    # while d is one of 'x', 'y', or 'z', denoting which side
    # of the cube. They are always in positive direction
    #
    # The cube coordinates denote the corner such that
    # the cube's diagonally opposite corner is at x+1,y+1,z+1.
    # So its 6 surfaces are:
    # (x, y, z, 'x')
    # (x, y, z, 'y')
    # (x, y, z, 'z')
    # (x-1, y, z, 'x')
    # (x, y-1, z, 'y')
    # (x, y, z-1, 'z')


    all_surfaces = set()
    blocked_surfaces = set()
    for l in lines:
        x, y, z = list(map(int, l.split(',')))
        for surface in getCubeSurfaces(x, y, z):
            if surface in all_surfaces:
                blocked_surfaces.add(surface)
            else:
                all_surfaces.add(surface)

    return len (all_surfaces - blocked_surfaces)

#           z
#           |    y
#           |  /
#           | /
#           |/
#           ------------ x
#
#

def getAdjacentSurfaces(x, y, z, d):
    if d == 'x':
        adjacents = [(x, y, z, 'y'),
                     (x, y, z, 'z'),
                     (x+1, y, z, 'y'),
                     (x+1, y, z, 'z'),
                     (x, y-1, z, 'y'),
                     (x, y, z-1, 'z'),
                     (x+1, y-1, z, 'y'),
                     (x+1, y, z-1, 'z')]

    D = {'x': (1,0,0),
         'y': (0,1,0),
         'z': (0,0,1)}

    dx, dy, dz = D[d]

    for d_ in set('xyz') - set(d):
      #             [(x, y, z, 'y'),
      #              (x, y, z, 'z'),
        adjacents += [(x, y, z, d_)]

      #              (x+1, y, z, 'y'),
      #              (x+1, y, z, 'z'),
        adjacents += [(x+dx, y+dy, z+dz, d_)]

      #              (x, y-1, z, 'y'),
      #              (x, y, z-1, 'z'),
        dx_, dy_, dz_ = D[d_]
        adjacents += [(x-dx_, y-dy_, z-dz_, d_)]
      #              (x+1, y-1, z, 'y'),
      #              (x+1, y, z-1, 'z')]
        adjacents += [(x+dx-dx_, y+dy-dy_, z+dz-dz_, d_)]

    return adjacents

def getCubeSurfaces(x, y, z):
    return ((x, y, z, 'x'),
            (x, y, z, 'y'),
            (x, y, z, 'z'),
            (x-1, y, z, 'x'),
            (x, y-1, z, 'y'),
            (x, y, z-1, 'z'))

def partB(filename: str) -> int:
    lines = getLines(filename)

    cube_surfaces = set()
    cubes = set()
    for l in lines:
        x, y, z = list(map(int, l.split(',')))
        cubes.add((x,y,z))

        for surface in getCubeSurfaces(x, y, z):
            cube_surfaces.add(surface)

    neighbors = (( 1,  0,  0),
                 ( 0,  1,  0),
                 ( 0,  0,  1),
                 (-1,  0,  0),
                 ( 0, -1,  0),
                 ( 0,  0, -1))

    min_ = min([min(a) for a in cubes])-1
    max_ = max([max(a) for a in cubes])+1

    SEEN = set((0,0,0))
    TO_VISIT = set([(0,0,0)])
    REACHABLE = set()

    while TO_VISIT:
        (x,y,z) = TO_VISIT.pop()

        for (dx, dy, dz) in neighbors:
            neighbor = (x+dx, y+dy, z+dz)

            if neighbor in SEEN:
                continue

            SEEN.add(neighbor)

            if any([xyz > max_ or xyz < min_ for xyz in neighbor]):
                continue

            if neighbor not in cubes:
                REACHABLE.add(neighbor)
                TO_VISIT.add(neighbor)

    REACHABLE_SURFACES = set()

    for block in REACHABLE:
        for surface in getCubeSurfaces(*block):
            REACHABLE_SURFACES.add(surface)

    return len(REACHABLE_SURFACES.intersection(cube_surfaces))

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