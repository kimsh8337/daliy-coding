import sys
sys.stdin = open('input.txt', 'r')

n = 1
while n!=0:
    n = int(input())
    ans = 0

    for i in range(n,2*n+1):
        cnt = 0
        for j in range(2,i+1):
            if i % j == 0:
                cnt += 1
                if cnt > 1:
                    break
        if cnt == 1:
            ans += 1
    print(ans)