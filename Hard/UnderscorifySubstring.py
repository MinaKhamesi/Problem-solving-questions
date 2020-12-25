def underscorifySubstring(string , substring):
    positions = collapse(getLocations(string, substring))
    return underscorify(string, positions)

def getLocations(string, substring):
    idxs = []
    idx = 0
    while idx < len(string) :
        nextIdx = string.find(substring, idx)
        if nextIdx != -1:
            idxs.append([nextIdx, nextIdx + len(substring)])
            idx = nextIdx + 1
        else:
            break
    return idxs

def collapse(idxs):
    if not len(idxs): return idxs
    finalIdxs = [idxs[0]]
    prev = finalIdxs[0]
    for i in range(1, len(idxs)):
        start, end = idxs[i]
        if start <= prev[1]:
            prev[1] = end
        else:
            finalIdxs.append([start, end])
            prev = finalIdxs[-1]
    return finalIdxs

def underscorify(string , positions):
    if not len(positions): return string
    newChar = []
    i , j = 0, 0
    currentPosition = positions[i][j]
    for idx,char in enumerate(string):
        if idx == currentPosition:
            newChar.append('_')

            if j == 1:
                i += 1
                j = 0
                currentPosition = positions[i][j] if i < len(positions) else -333
            else:
                j = 1
                currentPosition = positions[i][j]
        newChar.append(char)

    if positions[-1][-1] == len(string):
        newChar.append('_')
    return ''.join(newChar)
