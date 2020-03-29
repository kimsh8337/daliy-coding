import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,1+int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = [0] * n
    tmp = 0
    for i in range(m):
        ex = 0
        for j in range(n):
            if b[i] >= a[j]:
                if ex < a[j]:
                    ex = a[j]
                    cnt[j] += 1
    for i in range(n):
        if tmp < cnt[i]:
            tmp = cnt[i]
            ans = i+1
    print('#{} {}'.format(tc, ans))
