import sys
sys.stdin = open('input.txt', 'r')

def dfs(i=0,sum=0):
    global max_p
    if max_p > sum:
        return

    if i >= n or i+arr[i][0] > n:
        if max_p < sum:
            max_p = sum
        return
    else:
        for j in range(i,n):
            if j+arr[j][0] > n: continue
            dfs(j+arr[j][0], sum+arr[j][1])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_p = -float('inf')
dfs()
print(max_p)