
def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [parseLine(x.strip()) for x in lines]


def parseLine(line):
    return [x.split(' ') for x in line.split(' | ')]


def uniqueKeys(input):
    countMap = {}
    for v in input.values():
        countMap[v] = countMap.get(v, 0) + 1
    return [k for k, v in input.items() if countMap[v] == 1]


characterMap = {
    0: ['a', 'b', 'c', 'd', 'e', 'f'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

characterCounts = {k: len(characterMap[k]) for k in characterMap.keys()}


def part1(input):
    count = 0
    filterKeys = uniqueKeys(characterCounts)
    acceptableLengths = [len(characterMap[k]) for k in filterKeys]
    for i in input:
        count += len([x for x in i[1] if len(x) in acceptableLengths])
    return count


###############################################################################
def flatten(t):
    return [item for sublist in t for item in sublist]


def getStringWithLength(signalPatterns, length):
    return [x for x in signalPatterns if len(x) == length][0]


def remainingCharacters(stringX, stringY):
    return [x for x in list(stringX) if x not in list(stringY)]


def part2(input):
    filterKeys = uniqueKeys(characterCounts)
    acceptableLengths = [len(characterMap[k]) for k in filterKeys]

    # first get the 'a' character
    sevenCount = characterCounts[7]
    oneCount = characterCounts[1]
    fourCount = characterCounts[4]
    eightCount = characterCounts[8]
    # find example strings with the right length

    vals = []
    for i in input:
        sigPatterns = [sorted(x) for x in i[0]]
        one = getStringWithLength(sigPatterns, oneCount)
        seven = getStringWithLength(sigPatterns, sevenCount)
        four = getStringWithLength(sigPatterns, fourCount)
        eight = getStringWithLength(sigPatterns, eightCount)

        # can identify '6' if we can all the patterns of length 6
        sixPatterns = [x for x in sigPatterns if len(x) == 6]
        six = [x for x in sixPatterns if len(
            remainingCharacters(x, seven)) == 4][0]
        sixPatterns = [x for x in sixPatterns if x != six]

        fivePatterns = [x for x in sigPatterns if len(x) == 5]
        three = [x for x in fivePatterns if len(
            remainingCharacters(x, seven)) == 2][0]

        fivePatterns = [x for x in fivePatterns if x != three]
        five = [x for x in fivePatterns if len(
            remainingCharacters(x, six)) == 0][0]
        two = [x for x in fivePatterns if x != five][0]

        zero = [x for x in sixPatterns if len(
            remainingCharacters(x, three)) == 2][0]
        nine = [x for x in sixPatterns if len(
            remainingCharacters(x, three)) == 1][0]

        reverseLookup = {
            tuple(zero): 0,
            tuple(one): 1,
            tuple(two): 2,
            tuple(three): 3,
            tuple(four): 4,
            tuple(five): 5,
            tuple(six): 6,
            tuple(seven): 7,
            tuple(eight): 8,
            tuple(nine): 9
        }

        values = [reverseLookup[tuple(sorted(x))] for x in i[1]]
        vals.append(int(''.join([str(i) for i in values])))
    return sum(vals)


###############################################################################
testInput = readFile('./inputs/day08-test.in')
input = readFile('./inputs/day08.in')

print(f"    Day 8 - part 1 (Test) is: {part1(testInput)} ")
print(f"    Day 8 - part 1 is: {part1(input)} ")
print(f"    Day 8 - part 2 (Test) is: {part2(testInput)} ")
print(f"    Day 8 - part 2 is: {part2(input)} ")
