#time: O(nm*min(n,m)) | space: O(nm*min(n,m))
def longestCommonSubsequence(str1, str2):
	lcsTable = [[[] for i in range(len(str1) + 1)] for i in range(len(str2) + 1)]
	
	for row in range(1 , len(str2)  + 1):
		for  col in range(1, len(str1) + 1):
			if str1[col - 1] == str2[row - 1]:
				lcsTable[row][col] = lcsTable[row - 1][col - 1] + [str1[col - 1]]
			else:
				lcsTable[row][col] = max(lcsTable[row - 1][col], lcsTable[row][col - 1], key=len)
	return lcsTable[-1][-1]



##SOLUTION3 having odd and even lists to switch between that reduce space complexity to min(n,m)^2 , because we cannot have just two array and save just length to backtrack charachters later, we have to store the subsequences themselves in this solution.


## SOLUTION2 time:  O(nm) | space : O(nm)

def longestCommonSubsequence2(str1, str2):
    lengths = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1) :
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
    return buildSubsequence(lengths, str1)

def buildSubsequence(lengths, str1):
    sequence = []
    i = len(lengths) - 1
    j = len(lengths[0]) - 1
    while i != 0 and j != 0:
        if lengths[i][j] == lengths[i - 1][j]:
            i -= 1
        elif lengths[i][j] == lengths[i][j - 1]:
            j -= 1
        else:
            sequence.append(str1[j - 1])
            i -= 1
            j -= 1

    return list(reversed(sequence))
