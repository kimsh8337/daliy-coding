import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0):
    result = sorted(lotto)
    if i == 6:
        if result in ans: return
        else:
            ans.append(result)
        for a in range(6):
            print(result[a], end=' ')
        print()
        return

    for j in range(i,n):
        if visit[j]: continue
        visit[j] = 1
        lotto.append(s[j])
        backtrack(i+1)
        lotto.pop()
        visit[j] = 0

while 1:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    else:
        n = s.pop(0)
    lotto = []
    ans = []
    visit = [0]*n
    backtrack()
    print()

