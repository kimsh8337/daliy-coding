import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

def bfs(n, k):
    q = deque()
    q.append(n)

    while q:
        i = q.popleft()

        if i == k:
            return find[i]

        for j in (i+1, i-1, 2*i):
            if (0<=j<LIMIT) and find[j] == 0:
                find[j] = find[i] + 1
                q.append(j)

N, K = map(int, input().split())
LIMIT = 100001
find = [0] * LIMIT

print(bfs(N, K))