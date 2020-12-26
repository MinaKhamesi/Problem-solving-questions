#SOLUTION 1
#O(bns) time | O(n) space
def multiStringSearch(bigString, smallStrings):
    return [isInBig(bigString,smallString) for smallString in smallStrings]

def isInBig(big, small):
    for i in range(len(big)):
        if i + len(small) > len(big):break
        if isInBigHelper(big,small,i): return True
    return False

def isInBigHelper(big,small,start):
    leftSmall, rightSmall = 0, len(small) - 1
    leftBig, rightBig = start, start + len(small) - 1
    while leftSmall <= rightSmall:
        if small[leftSmall] != big[leftBig] or small[rightSmall] != big[rightBig]:
            return False
        leftSmall += 1
        rightSmall -= 1
        leftBig += 1
        rightBig -= 1
    return True

##SOLUTION2
## O(b^2 + ns) time | O(b^2 + n) space
def multiStringSearch2(bigString, smallStrings):
    trie = SuffixTrie(bigString)
    return [trie.contains(string) for string in smallStrings]

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.buildSuffixTrie(string)
    def buildSuffixTrie(self, string):
        for i in range(len(string)):
            current = self.root
            for j in range(i , len(string)):
                if string[j] not in current:
                    current[string[j]] = {}
                current = current[string[j]]
            
    def contains(self,string):
        current = self.root
        for char in string:
            if char not in current: return False
            current = current[char]
        return True

##SOLUTION3
#O( ns + bs ) time | O(ns) space
def multiStringSearch3(bigString, smallStrings):
    trie = Trie(smallStrings)
    stringsFound = {}
    for i in range(len(bigString)):
        searchThrough(bigString, i , stringsFound, trie)
    return [string in stringsFound for string in smallStrings]

class Trie:
    def __init__(self, strings):
        self.root = {}
        self.buildTrie(strings)

    def buildTrie(self, strings):
        for string in strings:
            current = self.root
            for char in string:
                if char not in current:
                    current[char] = {}
                current = current[char]
            current['*'] = string

def searchThrough(bigString, startIdx, stringsFound, trie):
    current = trie.root
    for i in range(startIdx , len(bigString)):
        if bigString[i] not in current:
            break
        else:
            current = current[bigString[i]]
            if '*' in current:
                stringsFound[current['*']] = True


