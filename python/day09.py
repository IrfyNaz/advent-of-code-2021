import math


def readFile(filename):
    with open(filename) as f:
        return [parseLine(x) for x in f.read().splitlines()]


def parseLine(line):
    return [int(x) for x in list(line)]


def part1(input):
    lenY = len(input)
    lenX = len(input[0])

    minPoints = []

    for y in range(lenY):
        for x in range(lenX):
            # check row above
            if y > 0:
                if input[y][x] >= input[y-1][x]:
                    continue
            if x > 0:
                if input[y][x] >= input[y][x-1]:
                    continue
            if y < lenY-1:
                if input[y][x] >= input[y+1][x]:
                    continue
            if x < lenX-1:
                if input[y][x] >= input[y][x+1]:
                    continue
            minPoints.append(input[y][x])

    return sum(minPoints) + len(minPoints)


###############################################################################

def gatherBasinPoints(input, x, y, checkedCoordinates):
    lenY = len(input)
    lenX = len(input[0])

    if (x, y) in checkedCoordinates:
        return [[], checkedCoordinates]

    basinPoints = []
    checkedList = checkedCoordinates
    checkedList.append((x, y))

    if input[y][x] == 9:
        return [basinPoints, checkedList]

    basinPoints.append(input[y][x])

    if x > 0 and not (x-1, y) in checkedList:
        points, checked = gatherBasinPoints(input, x-1, y, checkedList)
        basinPoints += points
        checkedList = checked
    if y < lenY - 1 and not (x, y+1) in checkedList:
        points, checked = gatherBasinPoints(input, x, y+1, checkedList)
        basinPoints += points
        checkedList = checked
    if y > 0 and not (x, y-1) in checkedList:
        points, checked = gatherBasinPoints(input, x, y-1, checkedList)
        basinPoints += points
        checkedList = checked

    if x < lenX - 1 and not (x+1, y) in checkedList:
        points, checked = gatherBasinPoints(input, x+1, y, checkedList)
        basinPoints += points
        checkedList = checked

    return [basinPoints, checkedList]


def part2(input):
    lenY = len(input)
    lenX = len(input[0])

    basins = []

    for y in range(lenY):
        for x in range(lenX):
            # check row above
            if y > 0:
                if input[y][x] >= input[y-1][x]:
                    continue
            if x > 0:
                if input[y][x] >= input[y][x-1]:
                    continue
            if y < lenY-1:
                if input[y][x] >= input[y+1][x]:
                    continue
            if x < lenX-1:
                if input[y][x] >= input[y][x+1]:
                    continue
            basin, checkedCoords = gatherBasinPoints(input, x, y, [])
            basins.append(basin)

    lengths = [len(x) for x in basins]

    return math.prod(sorted(lengths)[-3:])


###############################################################################
testInput = readFile('./inputs/day09-test.in')
input = readFile('./inputs/day09.in')

print(f"    Day 9 - part 1 (Test) is: {part1(testInput)} ")
print(f"    Day 9 - part 1 is: {part1(input)} ")
print(f"    Day 9 - part 2 (Test) is: {part2(testInput)} ")
print(f"    Day 9 - part 2 is: {part2(input)} ")
