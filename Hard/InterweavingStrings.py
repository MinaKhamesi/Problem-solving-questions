#O(2^(n+m)) time| O(n + m) space
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two) : return False
    return areInterwoven(one, two, three, 0 , 0)

def areInterwoven(one, two, three, idx1, idx2):
    idx3 = idx1 + idx2
    if idx3 == len(three): return True

    if idx1 < len(one) and one[idx1] == three[idx3]:
        found = areInterwoven(one, two, three, idx1 + 1, idx2)
        if found: return True
    if idx2 < len(two) and two[idx2] == three[idx3]:
        return areInterwoven(one, two, three, idx1, idx2 + 1)
    
    return False

#O(nm) time| O(nm) space
def interweavingStrings2(one, two, three):
    if len(three) != len(one) + len(two) : return False
    cache =[[None for i in range(len(two) + 1)] for j in range(len(one) + 1)]
    return areInterwoven2(one, two, three, 0 , 0, cache)

def areInterwoven2(one, two, three, idx1, idx2, cache):
    if cache[idx1][idx2]: return cache[idx1][idx2]
    idx3 = idx1 + idx2
    if idx3 == len(three): return True

    if idx1 < len(one) and one[idx1] == three[idx3]:
        cache[idx1][idx2] = areInterwoven2(one, two, three, idx1 + 1, idx2,cache)
        if cache[idx1][idx2]: return True
    if idx2 < len(two) and two[idx2] == three[idx3]:
        cache[idx1][idx2] = areInterwoven2(one, two, three, idx1, idx2 + 1,cache)
        return cache[idx1][idx2]
    
    cache[idx1][idx2] = False
    
    return False