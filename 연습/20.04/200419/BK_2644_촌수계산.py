import sys
sys.stdin = open('input.txt','r')
from _collections import deque

def bfs(start):
    q=deque()
    q.append(start)
    visit = [0 for _ in range(n+1)]
    visit[start] = 1
    while q:
        d = q.popleft()
        for i in s[d]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[d] + 1
                q.append(i)

n = int(input())
a,b = map(int,input().split())
m = int(input())
s = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]
for i in range(m):
    x,y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)
print(s)
bfs(a)

# print(result[b] if result[b] != 0 else -1)
if result[b] != 0:
    print(result[b])
else:
    print(-1)
