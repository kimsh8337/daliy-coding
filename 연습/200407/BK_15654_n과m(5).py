import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0):
    if i == m:
        for j in range(m):
            print(out[j],end = ' ')
        print()
        return

    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            out.append(nums[j])
            backtrack(i+1)
            out.pop()
            visited[j] = 0

n,m = map(int,input().split())
nums = list(map(int, input().split()))
visited = [0] * n
out = []

nums.sort()
backtrack()