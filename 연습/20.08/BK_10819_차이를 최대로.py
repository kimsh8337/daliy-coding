import sys
sys.stdin = open('input10819.txt', 'r')


def nextarr(s):
    k = -1
    for i in range(n-1):
        if s[i] < s[i+1]:
            k = i

    if k == -1:
        return -1

    for j in range(k+1, n):
        if s[j] > s[k]:
            m = j

    s[k], s[m] = s[m], s[k]
    tmp = s[k+1:]
    tmp.sort()

    return s[:k+1] + tmp


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
maxnum = 0

while 1:
    sum = 0
    for i in range(n-1):
        sum += abs(arr[i+1] - arr[i])

    maxnum = max(maxnum, sum)

    arr = nextarr(arr)
    if arr == -1:
        break

print(maxnum)