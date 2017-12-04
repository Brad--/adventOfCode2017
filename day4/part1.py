def getPhrases():
	phrases = []
	with open("data.txt", "r") as file:
	    for line in file:
	        phrases.append(line.split())
	return phrases

def validatePhrase(phrase):
	for (i, word) in enumerate(phrase):
		if word in phrase[i + 1:]:
			return False
	return True

def validPhrases():
	count = 0
	for phrase in getPhrases():
		if validatePhrase(phrase):
			count += 1
	return count

print(validPhrases())