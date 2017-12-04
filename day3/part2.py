import numpy as np

def calculateWidth(num):
    width = 1
    while (width * width) < num:
        width += 1
    return width

def initSpiral(num):
	width = calculateWidth(num)
	center = int(width / 2)
	spiral = np.zeros((width, width))
	spiral[center][center] = 1
	return spiral

def getSurrounding(spiral, row, col):
	total = 0
	topEdge  = row - 1 < 0
	leftEdge = col - 1 < 0
	bottomEdge = row + 1 >= spiral.shape[0]
	rightEdge  = col + 1 >= spiral.shape[0]

	if not topEdge:
		total += spiral[row - 1][col]
		if not leftEdge:
			total += spiral[row - 1][col - 1]
		if not rightEdge:
			total += spiral[row - 1][col + 1]
	if not bottomEdge:
		total += spiral[row + 1][col]
		if not leftEdge:
			total += spiral[row + 1][col - 1]
		if not rightEdge:
			total += spiral[row + 1][col + 1]
	if not leftEdge:
		total += spiral[row][col - 1]
	if not rightEdge:
		total += spiral[row][col + 1]

	return total


def calcSpiral(num):
	spiral = initSpiral(num)
	moves = ["R", "U", "L", "D"]
	max = 0

	steps = 1
	stepsUsed = False
	row = int(calculateWidth(num) / 2)
	col = row
	while max <= num:
		for move in moves:
			count = 0
			while count < steps:
				if move == "R":
					col += 1
				elif move == "L":
					col -= 1
				elif move == "U":
					row -= 1
				elif move == "D":
					row += 1
				spiral[row][col] = getSurrounding(spiral, row, col)
				if spiral[row][col] > max:
					max = spiral[row][col]
				if max > num:
					return max
				count += 1
			if stepsUsed:
				stepsUsed = False
				steps += 1
			else:
				stepsUsed = True

	# print(spiral)

print(calcSpiral(361527))