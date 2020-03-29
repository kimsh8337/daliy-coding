import sys
sys.stdin = open('input.txt', 'r')

m = int(input())
n = int(input())
ans = []
for i in range(m,n+1):
    cnt = 0
    for j in range(2,i+1):
        if i % j == 0:
            cnt += 1
            if cnt > 1:
                break
    if cnt == 1:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])