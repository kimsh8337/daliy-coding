import sys
sys.stdin = open('input.txt', 'r')

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def find(r,c,cnt,value):
    if cnt == 7:
        nums.add(value)
        return

    for a in range(4):
        nr = r + dr[a]
        nc = c + dc[a]
        if 0<=nr<4 and 0<=nc<4:
            find(nr,nc,cnt+1,value+str(arr[nr][nc]))
    return


for tc in range(1,int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    nums = set()

    for i in range(4):
        for j in range(4):
            find(i, j,1,str(arr[i][j]))

    print('#{} {}'.format(tc, len(nums)))