def longestStringChain( strings ):
    chains = {}
    maxLength = 0
    maxLengthStr = None
    sortedStrings = sorted(strings , key = len)
    for string in sortedStrings:
        chains[string] = {'longestThusFar': 0 , 'prevStr': None}
        for i in range(len(string)):
            newStr = string[:i] + string[i + 1:]
            if newStr in chains and chains[newStr]['longestThusFar'] + 1 > chains[string]['longestThusFar']:
                chains[string]['longestThusFar'] = chains[newStr]['longestThusFar'] + 1
                chains[string]['prevStr'] = newStr
        if chains[string]['longestThusFar'] > maxLength:
            maxLength = chains[string]['longestThusFar']
            maxLengthStr = string
    return [] if maxLength == 0 else buildSequence(chains , maxLengthStr)

def buildSequence(table , firstStr):
    result = []
    current = firstStr
    while current is not None:
        result.append(current)
        current = table[current]['prevStr']
    return result
