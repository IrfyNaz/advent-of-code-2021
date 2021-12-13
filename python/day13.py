from collections import defaultdict


def readFile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return parseLines(lines)


def parseLines(lines):
    coords = []
    instructions = []
    for l in lines:
        if l == '':
            continue
        if ',' in l:
            coords.append([int(x) for x in l.split(',')])
        else:
            instructions.append(l.replace('fold along ', '').split('='))
    return coords, instructions


def printGrid(grid):
    for row in grid:
        print(''.join(row))


def maxX(coords):
    return max([c[0] for c in coords])


def maxY(coords):
    return max([c[1] for c in coords])


def createGrid(coords):
    grid = [['.' for x in range(maxX(coords) + 1)]
            for y in range(maxY(coords) + 1)]

    for c in coords:
        grid[c[1]][c[0]] = '#'

    return grid


def countDots(grid):
    return sum([sum([1 for c in row if c == '#']) for row in grid])


def solve(coords, instructions):
    grid = createGrid(coords)

    for i in instructions:
        foldCoord = int(i[1])
        if i[0] == 'y':
            newGrid = grid[0:foldCoord]
            remaining = grid[foldCoord+1:][::-1]
        elif i[0] == 'x':
            newGrid = [[grid[y][x]
                        for x in range(foldCoord)] for y in range(len(grid))]
            remaining = [list(reversed([grid[y][x]
                                        for x in range(foldCoord+1, len(grid[0]))])) for y in range(len(grid))]

        for y in range(len(remaining)):
            for x in range(len(remaining[y])):
                newGrid[y][x] = remaining[y][x] if remaining[y][x] == '#' else newGrid[y][x]

        grid = newGrid
    printGrid(grid)
    return countDots(grid)


###############################################################################
testCoords, testInstructions = readFile('./inputs/day13-test.in')
coords, instructions = readFile('./inputs/day13.in')

print(
    f"    Day 13 - part 1 (Test) is: {solve(testCoords,[testInstructions[0]])} ")
print(f"    Day 13 - part 1 is: {solve(coords, [instructions[0]])} ")
print(f"    Day 13 - part 2 (Test) is: {solve(testCoords, testInstructions)} ")
print(f"    Day 13 - part 2 is: {solve(coords, instructions)} ")
