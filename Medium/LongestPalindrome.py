def longestPalindromicSubstring(string):
    longest = [0,1]
	
	for idx in range(len(string)-1):
		odd = getLongestPalindrome(idx-1,idx+1,string)
		even = getLongestPalindrome(idx,idx+1,string)
		currentLongest = max(odd,even,key = lambda x:x[1] - x[0])
		longest = max(longest,currentLongest,key=lambda x:x[1]-x[0])
		
	return string[longest[0]:longest[1]]

def getLongestPalindrome(leftIdx,rightIdx,string):
	while leftIdx>=0 and rightIdx<len(string) and string[leftIdx] == string[rightIdx]:
				leftIdx -= 1
				rightIdx += 1
	return [leftIdx+1,rightIdx]
