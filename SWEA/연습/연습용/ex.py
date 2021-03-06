import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0, sum = 0):
    global minsum, maxsum
    if i >= 12:
        if minsum > sum or minsum == -9999999:
            minsum = sum
        return

    backtrack(i+1, sum + price[0]*swimming[i])
    backtrack(i+1, sum + price[1])
    backtrack(i+3, sum + price[2])
    backtrack(i+12, sum + price[3])

T = int(input())

for tc in range(1,T+1):
    price = list(map(int, input().split()))
    swimming = list(map(int, input().split()))
    minsum = -9999999
    backtrack()
    print('#{} {}'.format(tc, minsum))
