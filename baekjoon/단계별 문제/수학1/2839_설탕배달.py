import sys
sys.stdin = open('input.txt','r')

n = int(input())
cnt = 0

while n>0:
    if n%5 != 0:
        n -= 3
        if n < 0:
            cnt = -1
            break
        cnt += 1
    elif n%5 == 0:
        cnt += 1
        n -= 5
    elif n %5 != 0 and n %3 != 0:
        cnt = -1
print(cnt)
