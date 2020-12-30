import sys
sys.stdin = open('input14888.txt', 'r')

def backtracking(i, sum):
    global maxans, minans

    if i == N-1:
        if maxans < sum:
            maxans = sum
        if minans > sum:
            minans = sum
        return

    for j in range(4):
        if carl[j] == 0:
            continue
        else:
            if j == 0:
                carl[j] -= 1
                backtracking(i+1, sum+A[i+1])
                carl[j] += 1
            elif j == 1:
                carl[j] -= 1
                backtracking(i+1, sum-A[i+1])
                carl[j] += 1
            elif j == 2:
                carl[j] -= 1
                backtracking(i+1, sum*A[i+1])
                carl[j] += 1
            else:
                carl[j] -= 1
                backtracking(i+1, int(sum/A[i+1]))
                carl[j] += 1


N = int(input())
A = list(map(int, input().split()))
carl = list(map(int, input().split()))

maxans = -float('inf')
minans = float('inf')

backtracking(0,A[0])

print(maxans)
print(minans)