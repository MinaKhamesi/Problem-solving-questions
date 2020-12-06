def levenshteinDistance(str1, str2):
    smallStr = str1 if len(str1) < len(str2) else str2
    bigStr = str1 if len(str1) >= len(str2) else str2
    minEditsNeeded_First = [i for i in range(len(smallStr) + 1)]
    minEditsNeeded_Second = [0 for i in range(len(smallStr) + 1)]
    for i in range(1,len(bigStr) + 1):
        if i%2 != 0:
            min_without_current_letter = minEditsNeeded_First
            current_min_to_calculate = minEditsNeeded_Second
        else:
            min_without_current_letter = minEditsNeeded_Second
            current_min_to_calculate = minEditsNeeded_First
        for  j in range(len(smallStr) + 1):
            if j==0 :
                current_min_to_calculate[j] = i
            elif smallStr[j - 1] == bigStr[i - 1]:
                current_min_to_calculate[j] = min_without_current_letter[ j - 1 ]
            else:
                current_min_to_calculate[j] = min(min_without_current_letter[j] , min_without_current_letter[j-1] , current_min_to_calculate[j -1 ]) + 1
    return minEditsNeeded_First[-1] if len(bigStr)%2 == 0 else minEditsNeeded_Second[-1]

#solution 2. The idea is the same but here we build the whole table
def levenshteinDistance2(str1, str2):
    minNumOfEdits = [[float('inf') for col in range(len(str1)+1)] for row in range(len(str2) + 1)]
    for col in range(len(str1) + 1):
        minNumOfEdits[0][col] = col
    for row in range(len(str2) + 1):
        minNumOfEdits[row][0] = row
    for row in range(1,len(str2) + 1):
        for col in range(1,len(str1) + 1):
            if str1[col - 1] != str2[row - 1]:
                minNumOfEdits[row][col] = min(minNumOfEdits[row-1][col], minNumOfEdits[row][col-1],minNumOfEdits[row - 1][col - 1]) + 1
            else:
                minNumOfEdits[row][col] = minNumOfEdits[row - 1][col - 1]
    return minNumOfEdits[-1][-1]