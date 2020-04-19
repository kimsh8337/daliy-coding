import sys
sys.stdin = open('input.txt','r')

for tc in range(1,1+int(input())):
    n,m = map(int, input().split())
    num = list(map(int, input().split()))
    sum = [0]*(n-m+1)

    for i in range(n-m+1):
        for j in range(i,i+m):
            sum[i] += num[j]

    print('#{} {}'.format(tc,max(sum)-min(sum)))