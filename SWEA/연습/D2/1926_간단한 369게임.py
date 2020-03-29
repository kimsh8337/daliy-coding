import sys
sys.stdin = open('input.txt', 'r')

num = int(input())

for i in range(1, num+1):
    sum = 0
    for j in str(i):
        if j in ['3', '6', '9']:
            sum += 1
    if sum == 0:
        print(i, end = ' ')
    else:
        print('-'*sum , end = ' ')
