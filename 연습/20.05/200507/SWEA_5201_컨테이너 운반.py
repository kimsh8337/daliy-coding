import sys
sys.stdin = open('input.txt','r')

for tc in range(1,1+int(input())):
    n,m = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    result = 0
    for i in range(m):
        for j in range(n):
            if truck[i] >= weight[j]:
                result += weight[j]
                weight[j] = 51
                break
    print('#{} {}'.format(tc, result))