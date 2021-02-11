import sys
sys.stdin = open('input.txt','r')
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    last = arr[-1]
    cnt = 0

    for i in range(len(arr)-1,-1,-1):
        if last > arr[i]:
            cnt += last-arr[i]
        else:
            last = arr[i]
    print('#{} {}'.format(tc, cnt))