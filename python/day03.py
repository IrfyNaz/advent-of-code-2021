def convertLineToInt(line):
    return [int(x) for x in line]


def readFile(filename):
    with open(filename) as f:
        return [convertLineToInt(list(x)) for x in f.read().splitlines()]


def binaryToDecimal(binary):
    return int(''.join(str(x) for x in binary), 2)


def decimalToBinary(decimal):
    return bin(decimal)[2:]


def gamma(counts, length):
    threshold = int(length / 2)
    ans = []
    ans = [0 for i in range(len(counts))]
    for idx, val in enumerate(counts):
        if val > threshold:
            ans[idx] = 1

    return ans


def epsilon(counts, length):
    threshold = int(length / 2)
    ans = []
    ans = [1 for i in range(len(counts))]
    for idx, val in enumerate(counts):
        if val > threshold:
            ans[idx] = 0

    return ans


def powerConsumption(gamma, epsilon):
    return binaryToDecimal(gamma) * binaryToDecimal(epsilon)


def part1(input):
    array = []
    array = [0 for i in range(len(input[0]))]
    for idx, val in enumerate(array):
        for x in input:
            array[idx] += x[idx]
    return powerConsumption(gamma(array, len(input)), epsilon(array, len(input)))


###############################################################################
def countOfValuesInArrayColumn(array, column):
    colVals = [x[column] for x in array]
    # count the number of instances of each value in colVals
    counts = {}
    for val in colVals:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
    return counts


def filterRows(inputs, starting, column):
    return [x for x in inputs if x[column] == starting]


def maxKey(dict):
    if (dict[0] == dict[1]):
        return 1
    return max(dict, key=dict.get)


def minKey(dict):
    if (dict[0] == dict[1]):
        return 0
    return min(dict, key=dict.get)


def oxGenRating(input):
    currentInputs = input
    newValue = []
    for x in range(len(input[0])):
        if(len(currentInputs) > 1):
            counts = countOfValuesInArrayColumn(currentInputs, x)
            maxValue = maxKey(counts)
            currentInputs = filterRows(currentInputs, maxValue, x)
    return currentInputs[0]


def co2ScrubRating(input):
    currentInputs = input
    for x in range(len(input[0])):
        if(len(currentInputs) > 1):
            counts = countOfValuesInArrayColumn(currentInputs, x)
            minValue = minKey(counts)
            currentInputs = filterRows(currentInputs, minValue, x)
    return currentInputs[0]


def part2(input):
    # oxygen generator rating
    ox = oxGenRating(input)
    co2 = co2ScrubRating(input)
    print(f" {ox} = {binaryToDecimal(ox)}")
    print(f" {co2} = {binaryToDecimal(co2)}")
    return(binaryToDecimal(ox) * binaryToDecimal(co2))


###############################################################################
testInput = readFile('./inputs/day03-test.in')
input = readFile('./inputs/day03.in')

print(f"    Day 3 - part 1 (Test) is: {part1(testInput)} ")
print(f"    Day 3 - part 1 is: {part1(input)} ")


print(f"    Day 3 - part 2 (Test) is: {part2(testInput)} ")
print(f"    Day 3 - part 2 is: {part2(input)} ")
