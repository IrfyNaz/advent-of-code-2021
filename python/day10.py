def readFile(filename):
    with open(filename) as f:
        return [list(x) for x in f.read().splitlines()]


def flatten(t):
    return [item for sublist in t for item in sublist]


CHAR_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

CHAR_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

COMPLETION_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def isCorrupted(line):
    badChars = []
    expectedChars = []
    for i in line:
        if i in CHAR_MAP.keys():
            expectedChars.append(CHAR_MAP[i])
        else:
            if i != expectedChars.pop():
                badChars.append(i)
    return {'incomplete': len(expectedChars) > 0, 'corrupt': len(badChars) > 0, 'badChars': badChars, 'missingChars': expectedChars}


def part1(input):
    corruptedLines = []
    for l in input:
        lineCheck = isCorrupted(l)
        if lineCheck['corrupt']:
            corruptedLines.append(lineCheck['badChars'])
    badChars = flatten(corruptedLines)
    scores = [CHAR_SCORES[i] for i in badChars]

    return sum(scores)


###############################################################################
def getLineScore(missingChars):
    score = 0
    for x in missingChars:
        score = (score * 5) + COMPLETION_SCORES[x]

    return score


def part2(input):
    corruptedLines = []
    incompleteLines = []
    for l in input:
        lineCheck = isCorrupted(l)
        if lineCheck['corrupt']:
            corruptedLines.append(lineCheck['badChars'])
        else:
            incompleteLines.append(lineCheck['missingChars'])
    scores = [getLineScore(i[::-1]) for i in incompleteLines]
    scores.sort()
    middleIndex = int((len(scores) - 1) / 2)
    score = scores[middleIndex]

    return score


###############################################################################
testInput = readFile('./inputs/day10-test.in')
input = readFile('./inputs/day10.in')

print(f"    Day 10 - part 1 (Test) is: {part1(testInput)} ")
print(f"    Day 10 - part 1 is: {part1(input)} ")
print(f"    Day 10 - part 2 (Test) is: {part2(testInput)} ")
print(f"    Day 10 - part 2 is: {part2(input)} ")
