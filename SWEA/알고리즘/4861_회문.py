import sys
sys.stdin = open('input.txt','r')

def check():
    for i in range(n):
        for j in range(n-m+1):
            tmp = words[i][j:j+m]
            if tmp == tmp[::-1]:
                return tmp

        for j in range(n-m+1):
            tmp = []
            for k in range(m):
                tmp.append(words[j+k][i])
            if tmp == tmp[::-1]:
                return tmp
    return []

for tc in range(1, 1+int(input())):
    n,m = map(int, input().split())
    words = [list(input()) for _ in range(n)]
    ans = check()
    print('#{} {}'.format(tc, ''.join(ans)))