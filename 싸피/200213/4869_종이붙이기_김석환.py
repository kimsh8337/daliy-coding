import sys
sys.stdin = open('input.txt', 'r')

def get_sum(x):
    if x == n:
        return 1
    if x>n:
        return 0
    return get_sum(x+10) + get_sum(x+20)*2

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    print('#{} {}'.format(tc, get_sum(0)))
