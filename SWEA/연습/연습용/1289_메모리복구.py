import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    num = list(map(int, input()))
    arr = [0]*len(num)
    cnt = 0

    for i in range(len(num)):
        if num[i] != arr[i] and num[i] == 1:
            for j in range(i,len(num)):
                arr[j] = 1
            cnt += 1
        elif num[i] != arr[i] and num[i] == 0:
            for j in range(i,len(num)):
                arr[j] = 0
            cnt +=1

    print('#{} {}'.format(tc, cnt))