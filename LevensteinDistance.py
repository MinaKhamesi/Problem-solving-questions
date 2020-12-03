def levenshteinDistance(str1, str2):
    minEditsNeeded_First = [i for i in range(len(str1) + 1)]
    minEditsNeeded_Second = [0 for i in range(len(str1) + 1)]
    for i in range(1,len(str2) + 1):
        if i%2 != 0:
            min_without_current_letter = minEditsNeeded_First
            current_min_to_calculate = minEditsNeeded_Second
        else:
            min_without_current_letter = minEditsNeeded_Second
            current_min_to_calculate = minEditsNeeded_First
        for  j in range(len(str1) + 1):
            if j==0 :
                current_min_to_calculate[j] = i
            elif str1[j - 1] == str2[i - 1]:
                current_min_to_calculate[j] = min_without_current_letter[ j - 1 ]
            else:
                current_min_to_calculate[j] = min(min_without_current_letter[j] , min_without_current_letter[j-1] , current_min_to_calculate[j -1 ]) + 1
    return minEditsNeeded_First[-1] if len(str2)%2 == 0 else minEditsNeeded_Second[-1]