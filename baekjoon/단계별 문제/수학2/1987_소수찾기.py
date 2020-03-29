import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
num = list(map(int, input().split()))

ans = 0
for i in range(n):
    cnt = 0
    for j in range(2,num[i]+1):
        if num[i] % j == 0:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)