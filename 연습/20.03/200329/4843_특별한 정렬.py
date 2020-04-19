import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # arr = sorted(arr,reverse=True)
    arr.sort(reverse=True)

    print('#{}'.format(tc), end = ' ')
    for i in range(5):
        print(arr[i], end = ' ')
        print(arr[n-i-1], end = ' ')
    print()