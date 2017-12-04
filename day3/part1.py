def calculateWidth(num):
    width = 1
    while (width * width) < num:
        width += 1
    return width

def getPosition(num, width, moves, row, col):
    curr = width * width
    while curr > 0:
        for move in moves:
            squares = 0
            while squares < width:
                if curr == num:
                    return (row, col)
                curr -= 1
                squares += 1
                if move == "L":
                    col -= 1
                elif move == "R":
                    col += 1
                elif move == "U":
                    row -= 1
                elif move == "D":
                    row += 1
            width -= 1
    return (row, col)
            

def getDistance(num):
    width = calculateWidth(num)

    if(width * width) % 2 == 1:
        #max val is bottom right
        moves = ["L", "U", "R", "D"]
        row = width
        col = width
    else:
        #max val is top left
        moves = ["R", "D", "L", "U"]
        row = 0
        col = 0
    targetRow, targetCol = getPosition(num, width, moves, row, col)
    print("target: ", targetRow, ", ", targetCol)

    onePos = width / 2
    rowDist = abs(targetRow - onePos)
    colDist = abs(targetCol - onePos)
    # -1 because zero based
    print(rowDist + colDist - 1)

getDistance(361527)