def getPhrases():
	phrases = []
	with open("data.txt", "r") as file:
	    for line in file:
	        phrases.append(line.split())
	return phrases

def isAnagram(curr, word):
	return sorted(curr) == sorted(word)

def validatePhrase(phrase):
	for (i, word) in enumerate(phrase):
		for curr in phrase[i + 1:]:
			if isAnagram(curr, word):
				return False
	return True

def validPhrases():
	count = 0
	for phrase in getPhrases():
		if validatePhrase(phrase):
			count += 1
	return count

print(validPhrases())