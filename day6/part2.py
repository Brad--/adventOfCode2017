def readData():
	data = []
	with open("data.txt", "r") as file:
	    for line in file:
	        data = [int(x) for x in line.split()]
	return data

def getDuplicateCycle(data):
	dupeFound = False
	cycles = [data[:]]

	while not dupeFound:
		listMax = max(data)
		index = data.index(listMax)
		data[index] = 0
		index += 1
		while listMax > 0:
			listMax -= 1
			data[index % len(data)] += 1
			index += 1
		if data in cycles:
			return data, len(cycles)
		else:
			cycles.append(data[:])

def getLoopSize():
	data, count = getDuplicateCycle(readData())
	data, count = getDuplicateCycle(data)
	return count

print(getLoopSize())