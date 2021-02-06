import sys
sys.stdin = open('input.txt', 'r')

n,s = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(s):
    min = arr[i]
    idx = i
    for j in range(i,n):
        if min > arr[j]:
            min = arr[j]
            idx = j
    arr[i], arr[idx] = min, arr[i]

for num in arr:
    print(num, end=" ")