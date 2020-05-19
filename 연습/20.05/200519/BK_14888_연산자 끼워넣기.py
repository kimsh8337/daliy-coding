import sys
sys.stdin = open('input14888.txt', 'r')


def dfs(i,res,plus,minus,multi,division):
    global max_num,min_num
    if i == n:
        max_num = max(max_num,res)
        min_num = min(min_num,res)
        return

    if plus:
        dfs(i+1,res+nums[i], plus-1,minus,multi,division)
    if minus:
        dfs(i + 1, res - nums[i], plus, minus-1, multi, division)
    if multi:
        dfs(i + 1, res * nums[i], plus, minus, multi-1, division)
    if division:
        dfs(i + 1, int(res/nums[i]), plus, minus, multi, division-1)



n = int(input())
nums = list(map(int, input().split()))
carl = list(map(int, input().split()))
max_num = -float('inf')
min_num = float('inf')
dfs(1,nums[0],carl[0],carl[1],carl[2],carl[3])
print(max_num)
print(min_num)