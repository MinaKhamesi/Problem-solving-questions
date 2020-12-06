class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
		
        for i in range(len(string)):
			current = self.root
			for j in range(i,len(string)):
				char = string[j]
				if char not in current:
					current[char] = {}
				current = current[char]
			current[self.endSymbol] = True
					

    def contains(self, string):
		current = self.root
        for char in string:
			if char not in current:
				return False
			current = current[char]
		return self.endSymbol in current
			
