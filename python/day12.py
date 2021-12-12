from collections import defaultdict


def readFile(filename):
    pathsMap = defaultdict(list)
    with open(filename) as f:
        instructionsRaw = [x.split('-') for x in f.read().splitlines()]
        for x, y in instructionsRaw:
            pathsMap[x].append(y)
            pathsMap[y].append(x)
    return pathsMap


def findEnd(nextSteps, pathsMap, pathsSoFar):
    paths = []
    for x in nextSteps:
        if x == 'start':
            continue

        if x == 'end':
            paths.append(pathsSoFar + [x])
            continue

        if x.islower():
            if x in pathsSoFar:
                continue

        solution = findEnd(pathsMap[x], pathsMap, pathsSoFar + [x])

        if solution:
            paths = paths + solution

    return paths


def part1(pathsMap):
    paths = findEnd(pathsMap['start'], pathsMap, ['start'])
    return len(paths)

###############################################################################


def findEndWithCount(nextSteps, pathsMap, pathsSoFar, maxVisits):
    paths = []
    for x in nextSteps:
        if x == 'start':
            continue

        if x == 'end':
            paths.append(pathsSoFar + [x])
            continue

        if x.islower():
            lowercase = [y for y in pathsSoFar if y.islower()]
            multipleVisits = [
                i for i in lowercase if lowercase.count(i) > maxVisits - 1]
            if len(multipleVisits):
                if x in pathsSoFar:
                    continue

        solution = findEndWithCount(
            pathsMap[x], pathsMap, pathsSoFar + [x], maxVisits)

        if solution:
            paths = paths + solution

    return paths


def part2(pathsMap):
    paths = findEndWithCount(pathsMap['start'], pathsMap, ['start'], 2)
    return len(paths)


###############################################################################
testInput = readFile('./inputs/day12-test.in')
testInput2 = readFile('./inputs/day12-test-2.in')
testInput3 = readFile('./inputs/day12-test-3.in')
input = readFile('./inputs/day12.in')

print(f"    Day 12 - part 1 (Test) is: {part1(testInput)} ")
print(f"    Day 12 - part 1 (Test 2) is: {part1(testInput2)} ")
print(f"    Day 12 - part 1 (Test 3) is: {part1(testInput3)} ")
print(f"    Day 12 - part 1 is: {part1(input)} ")
print(f"    Day 12 - part 2 (Test) is: {part2(testInput)} ")
print(f"    Day 12 - part 2 (Test 2) is: {part2(testInput2)} ")
print(f"    Day 12 - part 2 (Test 3) is: {part2(testInput3)} ")
print(f"    Day 12 - part 2 is: {part2(input)} ")
