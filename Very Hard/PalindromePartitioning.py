def palindromePartitioning( string ):
    palindromes = [[False for i in string] for j in string]
    for startIdx in range(len(string)):
        for endIdx in range(startIdx , len(string)):
            palindromes[startIdx][endIdx] = isPalindrome(string , startIdx, endIdx)
    minCuts = [float('inf') for endIdx in string]
    for endIdx in range(len(string)):
        if palindromes[0][endIdx]:
            minCuts[endIdx] = 0
        else:
            minCuts[endIdx] = minCuts[endIdx - 1] + 1
            for startIdx in range(1 , endIdx):
                if palindromes[startIdx][endIdx]:
                    minCuts[endIdx] = min(minCuts[endIdx] , minCuts[startIdx - 1] + 1)
    return minCuts[-1]
def isPalindrome(string , start , end):
    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True


def palindromePartitioning2( string ):
    palindromes = [[False for i in string] for j in string]
    for i in range(len(string)):
        palindromes[i][i] = True
    for length in range(2 , len(string) + 1):
        for startIdx in range(0 , len(string) - length + 1):
            endIdx = startIdx + length - 1
            if length == 2:
                palindromes[startIdx][endIdx] = string[startIdx] == string[endIdx]
            else:
                palindromes[startIdx][endIdx] = string[startIdx] == string[endIdx] and palindromes[startIdx + 1][endIdx - 1]
    minCuts = [float('inf') for endIdx in string]
    for endIdx in range(len(string)):
        if palindromes[0][endIdx]:
            minCuts[endIdx] = 0
        else:
            minCuts[endIdx] = minCuts[endIdx - 1] + 1
            for startIdx in range(1 , endIdx):
                if palindromes[startIdx][endIdx]:
                    minCuts[endIdx] = min(minCuts[endIdx] , minCuts[startIdx - 1] + 1)
    return minCuts[-1]