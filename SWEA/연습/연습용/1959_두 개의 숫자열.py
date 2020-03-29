import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n,m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    sum_list = []
    if n < m:
        for j in range(m-n+1):
            sum = 0
            for i in range(n):
                x = arr1[i] * arr2[j+i]
                sum += x
            sum_list.append(sum)
    elif n > m:
        for i in range(n-m+1):
            sum = 0
            for j in range(m):
                x = arr1[i+j] * arr2[j]
                sum += x
            sum_list.append(sum)
    elif n == m:
        for i in range(n):
            sum = 0
            for j in range(n):
                x = arr1[i] * arr2[j]
                sum += x
            sum_list.append(sum)

    print('#{} {}'.format(tc, max(sum_list)))