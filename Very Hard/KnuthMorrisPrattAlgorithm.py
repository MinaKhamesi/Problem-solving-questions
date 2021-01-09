def knuthMorrisPrattAlgorithm(string , substring):
    pattern = buildPattern(substring)
    return containsSubstring(string , substring , pattern)

def containsSubstring(string , substring , pattern):
    i , j = 0 , 0
    while i < len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return False

def buildPattern(string):
    pattern = [-1 for i in string]
    j = 0
    i = 1
    while i < len(string):
        if string[i] == string[j]:
            pattern[i] = j
            j += 1
            i += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern