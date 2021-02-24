import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

def bfs(a,b):
    q = deque()
    q.append((a,''))

    while q:
        num,li = q.popleft()

        if num == b:
            return li

        d = (num*2) % 10000
        if not visited[d]:
            visited[d] = 1
            q.append((d, li + 'D'))

        s = num-1
        if num == 0:
            s = 9999
        if not visited[s]:
            visited[s] = 1
            q.append((s,li+'S'))

        l = int(num%1000 * 10 + num / 1000)
        if not visited[l]:
            visited[l] = 1
            q.append((l,li+'L'))

        r = int(num%10*1000 + num//10)
        if not visited[r]:
            visited[r] = 1
            q.append((r,li+'R'))


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    visited = [0 for i in range(10000)]
    print(bfs(a,b))