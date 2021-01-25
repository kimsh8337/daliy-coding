total = 56
k = 23

from itertools import combinations_with_replacement

def ways(total,k):
    ans = 0
    nums = []

    for i in range(1,k+1):
        nums.append(i)

    for i in range(1,total+1):
        c = list(combinations_with_replacement(nums,i))
        for j in range(len(c)):
            if sum(c[j]) == total:
                ans += 1

    return ans


print(ways(total,k))