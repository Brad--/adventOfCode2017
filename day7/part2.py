class Program:
	def __init__(self, name, weight, holding):
		self.name = name
		self.weight = weight
		self.holding = holding

	def print(self):
		print("Name: ", self.name)
		print("Weight: ", self.weight)
		print("Holding: ", self.holding)

def readTree():
	items = []
	with open("test.txt") as stream:
		for line in stream:
			line = line.split()
			items.append(Program(line[0], int(line[1][1:len(line[1]) - 1]), [h.strip(",") for h in line[3:]]))
	itemsDict = {}
	for item in items:
		itemsDict[item.name] = item
	return items

def getTreeBase(tree):
	for program in tree:
		found = False
		for holder in tree:
			if program.name in holder.holding:
				found = True
		if not found:
			return program

def getProgramWeight(tree, programName, weight):
	disc = tree[programName].holding
	if disc:
		for program in disc:
			weight += getProgramWeight(tree, program.name, weight)
	else:
		return tree[programName].weight
	return weight + tree[programName].weight

def run():
	tree = readTree()
	base = getTreeBase(tree)
	base.print()
	#Find weight on trees
	#Track the last level
	#Track if the last level found an imbalance
	#If the last level found an imbalance, and there is no imbalance on the current disk, the last level has the imbalance

run()