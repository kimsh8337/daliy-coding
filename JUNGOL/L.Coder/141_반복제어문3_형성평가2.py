n = int(input())
num = 1
while (n*num)%10 != 0 and (n*num) < 100:
    print(n*num, end= ' ')
    num += 1
if n*num < 100:
    print(n*num)