import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i = 0, cnt = 0):
    if cnt == m:
        for j in range(m):
            print(out[j], end = ' ')
        print()
        return

    for j in range(n):
        out.append(nums[j])
        backtrack(j,cnt + 1)
        out.pop()

n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
out = []
backtrack()