def groupAnagrams(words):
	wordsTable = {}
    for word in words:
		key = "".join(sorted(word))
		if key not in wordsTable:
			wordsTable[key] = [word]
		else:
			wordsTable[key].append(word)
	return list(wordsTable.values())

