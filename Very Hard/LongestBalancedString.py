def longestBalancedString( string ):
    idxsStack = [-1]
    maxLength = 0
    for i in range(len(string)):
        char = string[i]
        if char == '(':
            idxsStack.append(i)
        else:
            idxsStack.pop()
            if len(idxsStack) == 0:
                idxsStack.append(i)
            else:
                startIdx = idxsStack[-1]
                currentLength = i - startIdx
                maxLength = max(maxLength , currentLength)
    return maxLength

def longestBalancedString2( string ):
    openingCount = 0
    closingCount = 0
    maxLength = 0
    for char in string:
        if char == '(':
            openingCount += 1
        else:
            closingCount += 1
        if openingCount == closingCount:
            maxLength = max(maxLength , closingCount * 2)
        if closingCount  > openingCount :
            openingCount = 0
            closingCount = 0
    openingCount = 0
    closingCount = 0
    for i in reversed(range(len(string))):
        char = string[i]
        if char == '(':
            openingCount += 1
        else:
            closingCount += 1
        if openingCount == closingCount:
            maxLength = max( maxLength , closingCount * 2)
        if openingCount > closingCount:
            openingCount = 0
            closingCount = 0
    return maxLength

def longestBalancedString3( string ):
    maxLength = 0
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1 , 2):
            if isBalanced(string , i , j):
                maxLength = max(maxLength , j - i)
    return maxLength

def isBalanced(string , i , j):
    stack = []
    for k in range(i , j):
        char = string[k]
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0
