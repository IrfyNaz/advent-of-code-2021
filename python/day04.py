def convertLineToInt(line):
    return [int(x) for x in line]

# First line is always the numbers that are going to be drawn
# followed by N boards of 5 x 5


MATCHED_CHAR = 'X'

# Read file and remove empty lines


def readFile(filename):
    with open(filename) as f:
        return [x for x in f.read().splitlines() if x != '']


def parseInput(input):
    drawnNumbers = [int(x) for x in input[0].split(',')]
    remainingLines = input[1:]
    boards = []
    for x in range(0, len(remainingLines), 5):
        board = []
        for i in range(0, 5):
            line = [int(x) for x in remainingLines[x+i].split(' ') if x != '']
            board.append(line)
        boards.append(board)

    return [drawnNumbers, boards]


def checkLineWin(line):
    win = True
    for x in range(5):
        win = win & (line[x] == MATCHED_CHAR)
    return win


def checkWin(board):
    # check rows and columns
    for x in range(5):
        # rows:
        lineWin = checkLineWin(board[x])
        if lineWin:
            return True
        # columns:
        column = []
        for y in range(5):
            column.append(board[y][x])
        lineWin = checkLineWin(column)
        if lineWin:
            return True
    return False


def boardSum(board):
    flattened = [
        item for sublist in board for item in sublist if item != MATCHED_CHAR]
    x = 0
    for y in flattened:
        x += y
    return x


def part1(drawnNumbers, boards):
    currentBoards = boards
    for x in drawnNumbers:
        newBoards = []
        # for each board:
        for b in currentBoards:
            board = []
            for l in b:
                line = []
                for v in l:
                    if x == v:
                        line.append(MATCHED_CHAR)
                    else:
                        line.append(v)
                board.append(line)
            newBoards.append(board)
        # Find all winning boards
        winningBoards = [x for x in newBoards if checkWin(x)]
        if len(winningBoards) > 0:
            boardScores = [boardSum(x) for x in winningBoards]
            winningScore = max(boardScores)
            return winningScore * x
        currentBoards = newBoards
    return 0


###############################################################################


def part2(drawnNumbers, boards):
    currentBoards = boards
    winningBoards = []
    for x in drawnNumbers:
        newBoards = []
        # for each board:
        for b in currentBoards:
            board = []
            for l in b:
                line = []
                for v in l:
                    if x == v:
                        line.append(MATCHED_CHAR)
                    else:
                        line.append(v)
                board.append(line)
            newBoards.append(board)
        # Find all winning boards
        winningBoards = [x for x in newBoards if checkWin(x)]
        currentBoards = [x for x in newBoards if not checkWin(x)]
        if len(currentBoards) == 0:
            boardScores = [boardSum(x) for x in winningBoards]
            winningScore = min(boardScores)
            return winningScore * x
    return 0


###############################################################################
testNumbers, testBoards = parseInput(readFile('./inputs/day04-test.in'))
drawnNumbers, boards = parseInput(readFile('./inputs/day04.in'))

print(f"    Day 4 - part 1 (Test) is: {part1(testNumbers, testBoards)} ")
print(f"    Day 4 - part 1 is: {part1(drawnNumbers, boards)} ")


print(f"    Day 4 - part 2 (Test) is: {part2(testNumbers, testBoards)} ")
print(f"    Day 4 - part 2 is: {part2(drawnNumbers, boards)} ")
