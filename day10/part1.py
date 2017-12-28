def readMoves():
	with open("data.txt") as stream:
		for line in stream:
			return [int(l) for l in line.split(",")]

def twist(moves, loopSize):
	loopSize += 1
	loop = list(range(0, loopSize))
	skipSize = 0
	pos = 0
	for move in moves:
		if move == 1:
			pos = (pos + move + skipSize) % loopSize
			skipSize += 1
			continue
		split = False
		end = pos + move

		print("Move: ", move, ", SkipSize: ", skipSize)
		print(loop)
		if end >= loopSize:
			split = True
			splitEnd = (end % loopSize)
			sublist = (loop[pos:] + loop[0:splitEnd])[::-1]
			print(sublist)
		else:
			loop[pos:end] = loop[pos:end][::-1]

		if split:
			loop[pos:] = sublist[0:splitEnd]
			loop[0:splitEnd] = sublist[splitEnd:]

		pos = (pos + move + skipSize) % loopSize
		skipSize += 1

		print(loop)
		print()
	return loop

def run():
	moves = readMoves()
	loop = twist([3, 4, 1, 5], 4)
	print(loop[0] * loop[1])
run()