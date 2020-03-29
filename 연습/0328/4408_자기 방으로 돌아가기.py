import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 1+int(input())):
    n = int(input())
    cnt = [0] * 201

    for i in range(n):
        a,b = map(int, input().split())

        a = (a+1)//2
        b = (b+1)//2

        if a > b:
            a,b = b,a
        for j in range(a,b+1):
            cnt[j] += 1

    print('#{} {}'.format(tc, max(cnt)))