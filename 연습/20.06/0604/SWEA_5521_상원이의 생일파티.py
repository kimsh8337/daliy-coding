import sys
sys.stdin = open('input5521.txt','r')

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    friend = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        friend[a].append(b)
        friend[b].append(a)

    sol = 0
    invited = [False] * (N + 1)
    invited[1] = True

    for i in range(len(friend[1])):
        f = friend[1][i]

        for j in range(len(friend[f])):
            if invited[friend[f][j]]: continue
            invited[friend[f][j]] = True
            sol += 1

        if invited[f]: continue
        invited[f] = True
        sol += 1

    print("#{} {}".format(tc, sol))