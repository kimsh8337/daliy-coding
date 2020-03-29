import sys
sys.stdin = open('input.txt', 'r')

m,n = map(int, input().split())

for i in range(m,n+1):
    cnt = 0
    for j in range(2,i+1):
        if i%j == 0:
            cnt += 1
            if cnt > 1:
                break
    if cnt == 1:
        ans = i
        print(ans)