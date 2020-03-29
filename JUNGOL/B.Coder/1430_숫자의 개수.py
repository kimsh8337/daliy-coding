import sys
sys.stdin = open('input.txt', 'r')

a = int(input())
b = int(input())
c = int(input())

ans = str(a*b*c)

for i in range(10):
    cnt = 0
    for j in range(len(ans)):
        if ans[j] == str(i):
            cnt += 1
    print(cnt)