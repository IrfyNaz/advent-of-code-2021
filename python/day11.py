def readFile(filename):
    with open(filename) as f:
        return [[int(y) for y in list(x)] for x in f.read().splitlines()]


def flatten(t):
    return [item for sublist in t for item in sublist]


def countAdjacent(x, y, grid):
    maxY = len(grid)
    maxX = len(grid[0])
    # check all adjacent cells
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x + i < 0 or x + i >= maxX:
                continue
            if y + j < 0 or y + j >= maxY:
                continue
            if grid[y + j][x + i] > 9:
                count += 1
    return count


def printGrid(grid):
    for y in grid:
        print(y)


def part1(grid, steps):
    maxY = len(grid)
    maxX = len(grid[0])
    countFlashes = 0
    # check all cells
    for i in range(steps):
        # First increment all values by one
        grid = [[min(a+1, 10) for a in b] for b in grid]
        newGrid = list(map(list, grid))
        # while there exists any values > 9 - flash + increment adjacent cells
        loop = True
        while(loop):
            newFlashCreated = False
            for y in range(maxY):
                for x in range(maxX):
                    if grid[y][x] > 9:
                        countFlashes += 1
                        newGrid[y][x] = -100
                    newGrid[y][x] += countAdjacent(x, y, grid)
                    if newGrid[y][x] > 9:
                        newFlashCreated = True
            grid = list(map(list, newGrid))

            if not newFlashCreated:
                loop = False
        grid = [[max(0, a) for a in b] for b in grid]

        print(' END OF STEP:')
        printGrid(grid)

    return countFlashes

###############################################################################


def part2(grid, steps):
    maxY = len(grid)
    maxX = len(grid[0])
    countFlashes = 0
    # check all cells
    for i in range(steps):
        # First increment all values by one
        grid = [[min(a+1, 10) for a in b] for b in grid]
        newGrid = list(map(list, grid))
        # while there exists any values > 9 - flash + increment adjacent cells
        loop = True
        while(loop):
            newFlashCreated = False
            for y in range(maxY):
                for x in range(maxX):
                    if grid[y][x] > 9:
                        countFlashes += 1
                        newGrid[y][x] = -100
                    newGrid[y][x] += countAdjacent(x, y, grid)
                    if newGrid[y][x] > 9:
                        newFlashCreated = True

            if(all(i < 0 for i in flatten(newGrid))):
                print('ALL VALUES FLASHED! {}'.format(i+1))
                return i + 1
            grid = list(map(list, newGrid))

            if not newFlashCreated:
                loop = False
        grid = [[max(0, a) for a in b] for b in grid]

    return 0


###############################################################################
testInputSmall = readFile('./inputs/day11-test-small.in')
testInput = readFile('./inputs/day11-test.in')
input = readFile('./inputs/day11.in')

print(f"    Day 11 - part 1 (Test) is: {part1(testInputSmall, 2)} ")
print(f"    Day 11 - part 1 (Test) is: {part1(testInput, 100)} ")
print(f"    Day 11 - part 1 is: {part1(input, 100)} ")
print(f"    Day 11 - part 2 (Test) is: {part2(testInput, 200)} ")
print(f"    Day 11 - part 2 is: {part2(input, 500)} ")
