import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,1+int(input())):
    arr = list(input())
    ans = []
    while 1:
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                arr.pop(i)
                arr.pop(i)
                break
        else:
            break

    print('#{} {}'.format(tc, len(arr)))