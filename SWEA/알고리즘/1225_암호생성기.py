import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    tc_num = int(input())
    secret = list(map(int, input().split()))

    num = 1
    while secret[-1] != 0:
        a = secret[0]
        if num > 5:
            num = 1
        a -= num
        if a < 0:
            a =0
        num += 1
        secret.append(a)
        secret.pop(0)

    print('#{}'.format(tc_num), end = ' ')
    for i in range(len(secret)):
        print(secret[i], end = ' ')
    print()