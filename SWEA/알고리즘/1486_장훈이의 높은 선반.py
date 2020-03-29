import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i, s):
    global ans
    if s >= b:
        if ans > s:
            ans = s
        return
    if i == n:
        return
    backtrack(i + 1, s + h[i])
    backtrack(i + 1, s)

T = int(input())
for tc in range(1, T + 1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 999999
    backtrack(0, 0)
    print('#{} {}'.format(tc,ans-b))