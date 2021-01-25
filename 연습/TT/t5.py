arr = [6,2,3,7,4,1,10]

import copy

def getMinimumMoves(arr):
    ans = 0
    num = 0
    arr2 = copy.deepcopy(arr)

    while 1:
        if arr == sorted(arr):
            break
        else:
            if num == 0:
                a = max(arr)
            arr.remove(a)
            arr2.remove(a)
            temp = a
            a = max(arr2)
            if num == 0:
                arr.append(temp)
            else:
                arr.insert(-num,temp)
            ans += 1
            num += 1

    return ans

print(getMinimumMoves(arr))