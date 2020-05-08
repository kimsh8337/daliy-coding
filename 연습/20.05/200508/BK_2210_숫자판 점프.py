import sys
sys.stdin = open('input.txt', 'r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def backtrack(r,c,i):
    global cnt

    if i == 6:
        tmp = com[:]
        if tmp in result:
            return
        else:
            result.append(tmp)
            cnt += 1
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<5 and 0<=nc<5:
            com.append(arr[r][c])
            backtrack(nr,nc,i+1)
            com.pop()

arr = [list(map(int, input().split())) for _ in range(5)]
result,com = [],[]
cnt = 0
for a in range(5):
    for b in range(5):
        backtrack(a,b,0)
print(cnt)