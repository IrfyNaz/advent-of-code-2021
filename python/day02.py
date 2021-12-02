
def parseInstruction(line):
    x, y = line.split(" ")
    return [x, int(y)]


def readFile(filename):
    with open(filename) as f:
        return [parseInstruction(x) for x in f.read().splitlines()]


def part1(input):
    x = 0  # horizontal
    y = 0  # depth
    for i, v in input:
        if i == "forward":
            x += v
        elif i == "up":
            y -= v
        elif i == "down":
            y += v

    return(x * y)


def part2(input):
    x = 0  # horizontal
    y = 0  # depth
    a = 0  # aim
    for i, v in input:
        if i == "forward":
            x += v
            y += a * v
        elif i == "up":
            a -= v
        elif i == "down":
            a += v

    return(x * y)


testInput = readFile('./inputs/day02-test.in')
input = readFile('./inputs/day02.in')

print(f"    Day 2 - part 1 (Test) is: {part1(testInput)} ")
print(f"    Day 2 - part 1 is: {part1(input)} ")


print(f"    Day 2 - part 2 (Test) is: {part2(testInput)} ")
print(f"    Day 2 - part 2 is: {part2(input)} ")
