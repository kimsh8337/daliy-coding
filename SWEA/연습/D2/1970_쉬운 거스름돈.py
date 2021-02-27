import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    price = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = []

    for i in money:
        n = price // i
        if n > 0:
            ans.append(n)
            price -= n * i
        else:
            ans.append(n)

    print('#{}'.format(tc))
    print(*ans)