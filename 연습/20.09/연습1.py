import sys
sys.stdin = open('input1.txt', 'r')


for tc in range(2):
    n = int(input())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    price = 100
    i, flag, sum = 0, 0, 0

    while(i < n):
        if p[i] >= c[i]:
            sum += price * c[i]
            flag = 0
            if flag == 0:
                price = 100
            if i == n-1:
                break
            p[i+1] += (p[i]-c[i])
            i += 1
        elif p[i] < c[i]:
            price = price // 2
            flag = 1
            if price < 25 or i == n-1:
                break
            p[i+1] += p[i]
            i += 1

    avg = round(sum / (i+1),2)
    print(str('%0.2f' %avg))
