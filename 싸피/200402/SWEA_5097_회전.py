import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 1+int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    print('#{}'.format(tc), end = ' ')
    for i in range(n):
        if m % n == i:
            print(arr[i])

