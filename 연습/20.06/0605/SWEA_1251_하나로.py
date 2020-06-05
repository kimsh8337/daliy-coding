import sys
sys.stdin=open('input1251.txt','r')

for t in range(1,int(input())+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    D = [0 for _ in range(N)]
    root = 0
    for i in range(1,N):
        D[i] = ((X[root] - X[i])**2 + (Y[root]-Y[i])**2) * E

    ans = 0
    visit = [0 for _ in range(N)]
    visit[root] = 1
    standard = 0

    for y in range(N - 1):
        minv = 12345678987654321
        for x in range(N):
            if not visit[x] and D[x] < minv:
                minv = D[x]
                standard = x

        ans += minv
        visit[standard] = 1
        root = standard

        for i in range(N):
            if not visit[i]:
                cost = ((X[root] - X[i])**2 + (Y[root]-Y[i])**2) * E
                if cost < D[i]:
                    D[i] = cost

    print('#{} {}'.format(t,round(ans)))