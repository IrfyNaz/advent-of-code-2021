from collections import defaultdict, Counter


def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        polymer = lines[0].strip()
        rules = {x: y.strip()
                 for x, y in [line.split(' -> ') for line in lines[2:]]}

    return polymer, rules


def part1(input, iterations):
    polymer, rules = input

    for i in range(iterations):
        newPolymer = polymer[0]
        for first, second in zip(polymer, polymer[1:]):
            newPolymer += rules[first + second] + second
        polymer = newPolymer

    counts = {x: polymer.count(x) for x in set(polymer)}
    minCount = min(counts, key=counts.get)
    maxCount = max(counts, key=counts.get)

    return counts[maxCount] - counts[minCount]


###############################################################################
def part2(input, iterations):
    polymer, rules = input
    pairCounts = Counter([''.join(pair) for pair in zip(polymer, polymer[1:])])

    for i in range(iterations):
        newPairs = Counter()
        duplicateCharAdjustment = Counter()

        for pair, insert in rules.items():
            # print("{} -> {} | {}".format(pair, insert, pairCounts[pair]))
            # The two new pairs created by the rule
            newPairs[pair[0] + insert] += pairCounts[pair]
            newPairs[insert + pair[1]] += pairCounts[pair]
            # The original pair no longer exists
            duplicateCharAdjustment[pair] += pairCounts[pair]

        for item in newPairs.keys():
            pairCounts[item] += newPairs[item]

        for item in duplicateCharAdjustment.keys():
            pairCounts[item] -= duplicateCharAdjustment[item]

    result = Counter(polymer[0])
    for pair in pairCounts:
        result[pair[1]] += pairCounts[pair]
    return result.most_common(1)[0][1] - result.most_common()[-1][1]


###############################################################################

testInput = readFile('./inputs/day14-test.in')
input = readFile('./inputs/day14.in')

print(f"    Day 14 - part 1 (Test) is: {part1(testInput, 10)}")
print(f"    Day 14 - part 1 is: {part1(input, 10)}")
print(f"    Day 14 - part 2 (Test) is: {part2(testInput, 40)} ")
print(f"    Day 14 - part 2 is: {part2(input, 40)} ")
