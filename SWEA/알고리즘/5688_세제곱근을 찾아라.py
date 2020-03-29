import sys
sys.stdin = open('input.txt','r')

arr = [i**3 for i in range(1000001)]

for tc in range(1, 1+int(input())):
    n = int(input())
    l,r = 1, 1000000
    ans = -1
    while l <= r:
        c = (l+r)//2
        if arr[c] == n:
            ans = c
            break
        if arr[c] < n:
            l = c+1
        else:
            r = c - 1
    print('#{} {}'.format(tc, ans))