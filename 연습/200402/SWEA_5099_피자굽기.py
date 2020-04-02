import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    n,m = map(int, input().split())
    c = list(map(int, input().split()))

    pizza = []
    r = -1

    for _ in range(n):
        r += 1
        pizza.append([r,c[r]])

    while len(pizza) != 1:
        i,j = pizza.pop(0)
        j //= 2
        if j != 0:
            pizza.append([i,j])
        if j == 0:
            if r < m-1:
                r += 1
                pizza.append([r,c[r]])

    print('#{} {}'.format(tc, pizza[0][0]+1))