import sys
sys.stdin = open('input.txt', 'r')

def promising(i):
    for j in range(0,i):
        if visit[j] == visit[i] or abs(visit[j]-visit[i]) == (i-j):
            return False
    return True

def backtrack(i=0):
    global cnt
    if i == n:
        cnt += 1
    else:
        for j in range(n):
            visit[i] = j
            if promising(i):
                backtrack(i+1)

n = int(input())
visit = [0] * n
cnt = 0
backtrack()
print(cnt)
