import sys
sys.stdin = open('input.txt', 'r')


def check(idx, value, cal, nums):
    global min_ans,max_ans

    if idx == n:
        if value < min_ans:
            min_ans = value
        if value > max_ans:
            max_ans = value
        return

    if cal[0] > 0:
        cal[0] -= 1
        check(idx+1, value+nums[idx], cal, nums)
        cal[0] += 1
    if cal[1] > 0:
        cal[1] -= 1
        check(idx+1, value-nums[idx], cal, nums)
        cal[1] += 1
    if cal[2] > 0:
        cal[2] -= 1
        check(idx+1, value*nums[idx], cal, nums)
        cal[2] += 1
    if cal[3] > 0:
        cal[3] -= 1
        check(idx+1, int(value/nums[idx]), cal, nums)
        cal[3] += 1
    return


for tc in range(1, int(input())+1):
    n = int(input())
    cal = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    min_ans = float('inf')
    max_ans = -float('inf')

    check(1,nums[0],cal,nums)

    print('#{} {}'.format(tc, max_ans-min_ans))