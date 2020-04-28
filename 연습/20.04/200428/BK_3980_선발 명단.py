import sys
sys.stdin = open('input.txt', 'r')

def dfs(i = 0, sum = 0):
    global max_sum

    if i == 11:
        if max_sum < sum:
            max_sum = sum
        return

    for j in range(11):
        if visited[j] == 1 or ability[i][j] == 0: continue
        visited[j] = 1
        dfs(i+1, sum + ability[i][j])
        visited[j] = 0


c = int(input())
for _ in range(c):
    ability = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    max_sum = -float('inf')
    dfs()
    print(max_sum)