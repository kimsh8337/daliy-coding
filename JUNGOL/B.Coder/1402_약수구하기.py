import sys
sys.stdin = open('input.txt','r')

n,k = map(int, input().split())
ans = []
for i in range(1,n+1):
    if n % i ==0:
        ans.append(i)
if len(ans) < k:
    print(0)
else:
    print(ans[k-1])