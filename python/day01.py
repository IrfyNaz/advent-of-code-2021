# solve aoc21 day 1
def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().splitlines()]

def countIncreasing(x):
  increasing = 0
  for a, b in zip(x, x[1:]):
    print(f" {a} {b}")
    if b > a:
      increasing += 1
  return increasing

def countIncreasingWindow(x, windowSize):
  increasing = 0
  for a, b in zip(x, x[windowSize:]):
    print(f" {a} {b} - {b > a}")
    if b > a:
      increasing += 1
  return increasing


testInput = readFile('../inputs/day01-test.in')
input = readFile('../inputs/day01.in')

print(f"    Test 1 part1 is: {countIncreasing(testInput)} ")
print(f"    Day 1 part1 is: {countIncreasing(input)} ")

print(f"    Test 1 part2 is: {countIncreasingWindow(testInput, 3)} ")
print(f"    Day 1 part2 is: {countIncreasingWindow(input, 3)} ")
