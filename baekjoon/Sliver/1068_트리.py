import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque


def leaf_node():
    q = deque()
    if nodes[-1]:
        q.append(nodes[-1][0])
    else:
        return 0
    cnt = 0

    while q:
        a = q.popleft()

        if len(nodes[a]) > 0:
            for k in range(len(nodes[a])):
                q.append(nodes[a][k])
        else:
            cnt += 1

    return cnt



n = int(input())
arr = list(map(int, input().strip().split()))
nodes = [[] for _ in range(n+1)]

for i in range(n):
    if arr[i] == -1:
       nodes[-1].append(i)
    else:
        nodes[arr[i]].append(i)

earse = int(input())

for i in range(n+1):
    if earse in nodes[i]:
        nodes[i].remove(earse)
        nodes[earse] = []

print(leaf_node())