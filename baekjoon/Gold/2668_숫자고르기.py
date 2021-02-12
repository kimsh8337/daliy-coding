import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(ed, st):
    visited[ed] = 1

    for num in card[ed]:
        if not visited[num]:
            dfs(num, st)
        elif visited[num] and num == st:
            res.append(num)

    return

n = int(input())
card = [[] for _ in range(n+1)]
for i in range(1,n+1):
    card[i].append(int(input()))
res = []

for i in range(1,n+1):
    visited = [0]*(n+1)
    dfs(i,i)

print(len(res))
for i in range(len(res)):
    print(res[i])