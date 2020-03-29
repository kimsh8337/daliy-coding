import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
ans = 0

for i in range(1,n+1):
    m = 0
    a = str(i)
    for j in range(len(a)):
        m += int(a[j])
    if ans < i and ans ==0:
        if n == m + i:
            ans = i
print(ans)