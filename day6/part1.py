def readData():
	data = []
	with open("data.txt", "r") as file:
	    for line in file:
	        data = [int(x) for x in line.split()]
	return data

def getDuplicateCycle():
	data = readData()
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
			dupeFound = True
		else:
			cycles.append(data[:])

	return len(cycles)

print(getCycles())