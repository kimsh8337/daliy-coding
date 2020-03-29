import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    arr = list(input())
    pole = 0
    cnt = 0

    for i in range(len(arr)-1):
        if arr[i] == '(' and arr[i+1] == ')':
            cnt += pole
        elif arr[i] == '(':
            pole += 1
            cnt += 1
        elif arr[i] == ')' and arr[i-1] != '(':
            pole -= 1

    print('#{} {}'.format(tc, cnt))
