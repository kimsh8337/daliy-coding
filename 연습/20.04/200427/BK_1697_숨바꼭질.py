import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

def bfs(arr, n, k):
    q = deque()
    q.append(n)

    while q:
        i = q.popleft()

        if i == k:
            return arr[i]

        for j in (i+1, i-1, 2*i):
            if (0<=j<LIMIT) and arr[j] == 0:
                arr[j] = arr[i] + 1
                q.append(j)

N, K = map(int, input().split())
LIMIT = 100001
find = [0] * LIMIT

print(bfs(find, N, K))