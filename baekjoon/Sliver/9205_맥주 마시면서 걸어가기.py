import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs(x,y):
    q, c = deque(), []
    q.append((x,y,20))
    c.append((x,y,20))
    while q:
        x,y,beer = q.popleft()

        if x == x1 and y == y1:
            print('happy')
            return
        for nx,ny in d:
            if (nx,ny,20) not in c:
                li = abs(nx-x) + abs(ny-y)
                if beer*50 >= li:
                    q.append((nx,ny,20))
                    c.append((nx,ny,20))
    print('sad')


for tc in range(int(input())):
    n = int(input())
    x0,y0 = map(int, input().split())
    d = []
    for _ in range(n):
        x, y = map(int, input().split())
        d.append((x,y))
    x1,y1 = map(int, input().split())
    d.append((x1,y1))
    bfs(x0,y0)