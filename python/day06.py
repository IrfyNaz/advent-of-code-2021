
def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [parseFish(int(x)) for x in lines[0].split(',')]


def flatten(listOfLists):
    return


def parseFish(input):
    return createFish(input, 6, 2)


def createFish(daysLeft, resetDays, newFishBuffer):
    return {'daysLeft': daysLeft, 'resetDays': resetDays, 'newFishBuffer': newFishBuffer}


def part1(input, cycles):
    fish = input

    for i in range(cycles):
        newFish = []
        for x in fish:
            newDaysLeft = x['daysLeft'] - 1
            if newDaysLeft < 0:
                newFish.append(createFish(
                    x['resetDays'], x['resetDays'], x['newFishBuffer']))
                newFish.append(createFish(
                    x['resetDays'] + x['newFishBuffer'], x['resetDays'], x['newFishBuffer']))
            else:
                newFish.append(createFish(
                    newDaysLeft, x['resetDays'], x['newFishBuffer']))
        fish = newFish

    return len(fish)


###############################################################################


def part2(input, cycles):
    fish = input
    fish = [x['daysLeft'] for x in fish]
    fishCounts = [0,0,0,0,0,0,0,0,0]
    for x in fish:
        fishCounts[x] += 1

    for i in range(cycles):
        fishCounts.append(fishCounts.pop(0))
        fishCounts[6] += fishCounts[8]
    return sum(fishCounts)


###############################################################################
testInput = readFile('./inputs/day06-test.in')
input = readFile('./inputs/day06.in')

print(f"    Day 6 - part 1 (Test) is: {part1(testInput, 80)} ")
print(f"    Day 6 - part 1 is: {part1(input, 80)} ")
print(f"    Day 6 - part 2 (Test) is: {part2(testInput, 256)} ")
print(f"    Day 6 - part 2 is: {part2(input, 256)} ")