def getJumps():
	jumps = []
	with open("data.txt", "r") as file:
	    for jump in file:
	        jumps.append(int(jump))
	return jumps

def interruptEscape():
	steps = 0
	jumps = getJumps()
	done = False
	pos = 0
	
	while not done:
		toMove = jumps[pos]

		if toMove >= 3:
			jumps[pos] -= 1
		else:
			jumps[pos] += 1

		steps += 1
		if toMove != 0:
			landing = pos + toMove
			if landing >= 0 and landing < len(jumps):
				pos = landing
			else:
				return steps

print(interruptEscape())