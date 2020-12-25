def longestSubstringWithoutDuplication(string):
    lastSeen = {}
    startIdx = 0
    longest = [0 , 1]
    for endIdx, currentChar in enumerate(string):
        if currentChar in lastSeen:
            startIdx = max(startIdx , lastSeen[currentChar] + 1)
        if endIdx + 1 - startIdx > longest[1] - longest[0]:
            longest = [startIdx, endIdx + 1]
        lastSeen[currentChar] = endIdx
    return string[longest[0] : longest[1]]
        