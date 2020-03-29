import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i = 0, sum=0):
    global max_sum, min_sum, cnt
    if i==n:
        if max_sum < sum or max_sum == 9999999999:
            max_sum = sum
        if min_sum > sum or min_sum == -199999:
            min_sum = sum
        return

    for j in range(len(lst)):
        if lst[j] != 0:
            lst[j] -= 1
            if j == 0:
                backtrack(i+1, sum + num[i])
            elif j == 1:
                backtrack(i+1, sum - num[i])
            elif j == 2:
                backtrack(i+1, sum * num[i])
            elif j == 3:
                backtrack(i+1, int(sum / num[i]))
            lst[j] += 1

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    num = list(map(int, input().split()))
    max_sum = 9999999999
    min_sum = -199999
    cnt = 0
    backtrack(1,num[0])
    print('#{} {}'.format(tc, max_sum-min_sum))