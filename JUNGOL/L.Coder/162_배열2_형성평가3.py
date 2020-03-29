import sys
sys.stdin = open('input.txt', 'r')

a,b = map(int, input().split())
arr = [0]*10
arr[0],arr[1] = a,b

for i in range(2,10):
    c = (arr[i-2]+arr[i-1])%10
    arr[i] = c

for i in range(10):
    print(arr[i], end = ' ')