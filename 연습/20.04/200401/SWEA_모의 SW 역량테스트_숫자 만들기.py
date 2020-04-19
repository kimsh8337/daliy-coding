import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i,sum):
    global max_sum, min_sum
    if i == n:
        if max_sum < sum:
            max_sum = sum
        if min_sum > sum:
            min_sum = sum
        return

    for j in range(len(operator)):
        if operator[j] == 0:
            continue
        else:
            operator[j] -= 1
            if j==0:
                backtrack(i+1,sum+nums[i])
            elif j==1:
                backtrack(i+1,sum-nums[i])
            elif j==2:
                backtrack(i+1,sum*nums[i])
            elif j==3:
                backtrack(i+1,int(sum/nums[i]))
            operator[j] += 1

for tc in range(1, 1+int(input())):
    n = int(input())
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    max_sum = -float('inf')
    min_sum = float('inf')
    backtrack(1,nums[0])
    print('#{} {}'.format(tc, max_sum-min_sum))