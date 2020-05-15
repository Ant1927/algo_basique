import copy


def lcss(a, b, best_lcss=[], crt_lcss=[]):
    if len(a) == 0 or len(b) == 0:
        if len(crt_lcss) > len(best_lcss):
            best_lcss = crt_lcss.copy()
        return best_lcss
    for i in range(len(a)):
        if a[i] in b:
            crt_lcss.append(a[i])
            best_lcss = lcss(a[i + 1:], b[b.index(a[i]) + 1:], best_lcss, crt_lcss)
            crt_lcss.pop()
    return best_lcss


def lciss(a, best_lciss=[], crt_lciss=[]):
    if len(a) == 0:
        if len(crt_lciss) > len(best_lciss):
            best_lciss = copy.deepcopy(crt_lciss)
        return best_lciss
    for i in range(len(a)):
        if len(crt_lciss) == 0:
            crt_lciss.append(a[i])
            best_lciss = lciss(a[i + 1:], best_lciss, crt_lciss)
            crt_lciss.pop()
        else:
            if a[i] > crt_lciss[-1]:
                crt_lciss.append(a[i])
                best_lciss = lciss(a[i + 1:], best_lciss, crt_lciss)
                crt_lciss.pop()
    return best_lciss


str1 = "AGGTAB"
str2 = "GXTXAYB"
best_lcss = []
best_lcss = lcss(str1, str2)
print('The longest sequence is : ' + "".join(best_lcss))

list_sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
best_lciss = lciss(list_sequence)
print('The longest increasing sequence is : ', best_lciss)
