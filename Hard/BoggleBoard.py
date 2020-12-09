def boggleBoard(board, words):
    trie = Trie(words)
    visiting = [[False for col in board[0]] for row in board]
    result = {}
	for row in range(len(board)):
		for col in range(len(board[row])):
			explore(board, row, col, visiting, result, trie.root
	return list(result.keys())



def explore(board, row, col, visiting, result, root):
	if isOutOfBound(board, row, col): return
	if visiting[row][col]: return
	currentLetter = board[row][col]
	if currentLetter not in root: return
	visiting[row][col] = True
	nextRoot = root[currentLetter]
	if '*' in nextRoot:
			result[nextRoot['*']] = True
			
	for [i,j] in getNeighbors(row,col):
		explore(board,i, j , visiting, result, root[currentLetter])
	visiting[row][col] = False
	
def isOutOfBound(board,row, col):
	return row < 0 or col < 0 or row >= len(board) or col >= len(board[0])
	
def getNeighbors(row, col):
	return [[row, col+1],[row, col -1], [row + 1, col], [row - 1, col], [row+1, col + 1], [row + 1, col - 1], [row - 1, col + 1],[row - 1, col - 1]]
	
	
class Trie:
	def __init__(self,words):
		self.root = {}
		self.populateTrie(words)
		
	def populateTrie(self, words):
		for word in words:
			current = self.root
			for letter in word:
				if letter not in current:
					current[letter] = {}
				current = current[letter]
			current['*'] = word
			
