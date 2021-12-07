
def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [int(x) for x in lines[0].split(',')]


def part1(crabs):
    minPos = min(crabs)
    maxPos = max(crabs)
    newPos = [0] * (maxPos + 1)
    for i in range(minPos, maxPos+1):
        newPos[i] = sum([abs(i - x) for x in crabs])

    return min(newPos)


###############################################################################
def sumOfIncreasingNumbers(x):
    return sum(range(0, x+1))


def part2(crabs):
    minPos = min(crabs)
    maxPos = max(crabs)
    newPos = [0] * (maxPos + 1)
    for i in range(minPos, maxPos+1):
        newPos[i] = sum([sumOfIncreasingNumbers(abs(i - x)) for x in crabs])

    return min(newPos)


###############################################################################
testInput = readFile('./inputs/day07-test.in')
input = readFile('./inputs/day07.in')

print(f"    Day 7 - part 1 (Test) is: {part1(testInput)} ")
print(f"    Day 7 - part 1 is: {part1(input)} ")
print(f"    Day 7 - part 2 (Test) is: {part2(testInput)} ")
print(f"    Day 7 - part 2 is: {part2(input)} ")
