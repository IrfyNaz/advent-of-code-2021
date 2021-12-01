# solve aoc21 day 1
def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().splitlines()]

def countIncreasing(x):
  increasing = 0
  for a, b in zip(x, x[1:]):
    if b > a:
      increasing += 1
  return increasing

def countIncreasingWindow(x, windowSize):
  increasing = 0
  for a, b in zip(x, x[windowSize:]):
    if b > a:
      increasing += 1
  return increasing

testInput = readFile('../inputs/day01-test.in')
input = readFile('../inputs/day01.in')

print(f"    Day 1 - part 1 (Test) is: {countIncreasing(testInput)} ")
print(f"    Day 1 - part 1 is: {countIncreasing(input)} ")

print(f"    Day 1 - part 2 (Check for part 1 / test) is: {countIncreasingWindow(testInput, 1)} ")
print(f"    Day 1 - part 2 (Check for part 1) is: {countIncreasingWindow(input, 1)} ")
print(f"    Day 1 - part 2 (Test) is: {countIncreasingWindow(testInput, 3)} ")
print(f"    Day 1 - part 2 is: {countIncreasingWindow(input, 3)} ")
