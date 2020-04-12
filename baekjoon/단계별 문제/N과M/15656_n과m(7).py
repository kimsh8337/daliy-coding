import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i = 0):
    if i == m:
        for j in range(m):
            print(out[j], end = ' ')
        print()
        return

    for j in range(n):
        out.append(nums[j])
        backtrack(i + 1)
        out.pop()

n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
out = []
backtrack()