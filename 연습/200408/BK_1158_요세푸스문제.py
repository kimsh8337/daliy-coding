import sys
sys.stdin=open('input.txt', 'r')
from _collections import deque

n,k = map(int, input().split())
q = deque(i for i in range(1,n+1))
out = []

while q:
    for _ in range(k-1):
        r = q.popleft()
        q.append(r)
    r = q.popleft()
    out.append(r)

print('<',end = '')
for i in range(n):
    if i < n-1:
        print(out[i],end =', ')
    else:
        print(out[i], end = '')
print('>')



