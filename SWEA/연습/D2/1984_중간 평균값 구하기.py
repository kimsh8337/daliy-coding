import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    num = list(map(int, input().split()))
    num_list = sorted(num)
    sum = 0
    for i in range(1,len(num_list)-1):
        sum += num_list[i]
    avg = sum/(len(num_list)-2)
    print('#{} {}'.format(tc, round(avg)))