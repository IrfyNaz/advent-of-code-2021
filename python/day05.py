def convertLineToInt(line):
    return [int(x) for x in line]

# Read file and remove empty lines


def readFile(filename):
    with open(filename) as f:
        return [parseLine(x) for x in f.read().splitlines()]


def parseLine(line):
    return [parseCoordinates(x) for x in line.split(' -> ')]


def parseCoordinates(coords):
    return [int(x) for x in coords.split(',')]


def flatten(listOfLists):
    return [item for sublist in listOfLists for item in sublist]


def part1(input):
    gridSize = max(flatten(flatten(input))) + 1
    grid = [[0] * gridSize for _ in range(gridSize)]
    # This should only check vertical or horizontal lines
    for line in input:
        x0, y0 = line[0]
        x1, y1 = line[1]
        xs = [x0, x1]
        ys = [y0, y1]
        if x0 == x1 or y0 == y1:
            xs.sort()
            ys.sort()
            for x in range(xs[0], xs[1]+1):
                for y in range(ys[0], ys[1]+1):
                    grid[x][y] += 1

    allCounts = [x for x in flatten(grid) if x > 1]
    return len(allCounts)


###############################################################################


def part2(input):
    gridSize = max(flatten(flatten(input))) + 1
    grid = [[0] * gridSize for _ in range(gridSize)]
    # This should only check vertical or horizontal lines
    for line in input:
        x0, y0 = line[0]
        x1, y1 = line[1]
        xs = [x0, x1]
        ys = [y0, y1]
        if x0 == x1 or y0 == y1:
            xs.sort()
            ys.sort()
            for x in range(xs[0], xs[1]+1):
                for y in range(ys[0], ys[1]+1):
                    grid[x][y] += 1
        else:
            xMult = 1 if x0 < x1 else -1
            yMult = 1 if y0 < y1 else -1
            for i in range(0, abs(x0 - x1) + 1):
                grid[x0 + (i * xMult)][y0 + (i * yMult)] += 1

    allCounts = [x for x in flatten(grid) if x > 1]
    return len(allCounts)


###############################################################################
testInput = readFile('./inputs/day05-test.in')
input = readFile('./inputs/day05.in')

print(f"    Day 5 - part 1 (Test) is: {part1(testInput)} ")
print(f"    Day 5 - part 1 is: {part1(input)} ")


print(f"    Day 5 - part 2 (Test) is: {part2(testInput)} ")
print(f"    Day 5 - part 2 is: {part2(input)} ")
