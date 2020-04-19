import sys
sys.stdin = open('input.txt','r')

def backtrack(i=0):
    if i == m:
        for j in range(m):
            print(out[j], end=' ')
        print()
        return

    for j in range(n):
        if j==0 or nums[j-1] != nums[j] or visited[j-1]:
            visited[j] = 1
            out.append(nums[j])
            backtrack(i+1)
            visited[j] = 0
            out.pop()

n,m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0]*n
out = []
backtrack()