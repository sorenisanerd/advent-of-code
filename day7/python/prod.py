class Directory(object):
    def __init__(self, parent=None):
        self.subdirectories = {}
        self.files = {}
        self.parent = parent

    def add_file(self, size, name):
        self.files[name] = size

    def add_directory(self, name):
        self.subdirectories[name] = Directory(self)

    def total(self):
        total = 0
        for subdir in self.subdirectories:
            total += self.subdirectories[subdir].total()
        for file in self.files:
            total += self.files[file]
        return total

    def walk_subdirectories(self, func):
        func(self)
        for d in self.subdirectories:
            self.subdirectories[d].walk_subdirectories(func)


def parseDirectoryStructure(lines: list) -> Directory:
    state = 'UNKNOWN'
    for l in lines:
        if l[0] == '$':
            state = 'CMDLINE'
        if state == 'CMDLINE':
            assert l[0] == '$'
            cmdline = l[2:]
            argv = cmdline.split(' ')
            cmd = argv[0]
            if cmd == 'cd':
                if argv[1] == '/':
                    curdir = root
                    continue
                elif argv[1][0] == '/':
                    assert False
                elif argv[1] == '..':
                    curdir = curdir.parent
                else:
                    curdir = curdir.subdirectories[argv[1]]
                    continue
            elif cmd == 'ls':
                state = 'LIST'
                continue
            else:
                assert False
        elif state == 'LIST':
            size, name = l.split(' ')
            if size == 'dir':
                curdir.add_directory(name)
                continue
            curdir.add_file(int(size), name)
    return root

root = Directory()
total_size_of_directories_under_100000 = 0

def partA(filename: str) -> int:
    lines = getLines(filename)
    parseDirectoryStructure(lines)
    curdir = root

    global tota_size_of_directories_under_100000

    def f(d):
        global total_size_of_directories_under_100000
        total = d.total()
        if total < 100000:
            total_size_of_directories_under_100000 += total

    root.walk_subdirectories(f)
    return total_size_of_directories_under_100000


def partB(filename: str) -> int:
    lines = getLines(filename)
    curdir = root
    parseDirectoryStructure(lines)

    global dirsizes
    dirsizes = []

    def f(d):
        global dirsizes
        total = d.total()
        dirsizes += [total]

    root.walk_subdirectories(f)
    dirsizes = sorted(dirsizes)

    used_capacity = root.total()
    for x in dirsizes:
        if x > used_capacity-40000000:
            return x

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
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))