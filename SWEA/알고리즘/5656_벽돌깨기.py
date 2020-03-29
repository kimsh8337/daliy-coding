import sys
sys.stdin = open('input.txt', 'r')

def backtrack(i=0):
    global max_sum, sum
    if i == n:
        if max_sum < sum or max_sum == -1:
            max_sum = sum
            sum = 0
        return

    for a in range(m):
        for b in range(h):
            if block[a][b] != 0:
                if block[a][b] == 1:
                    sum += 1
                    block[a][b] = 0
                    backtrack(i+1)
                    block[a][b] = 1
                elif block[a][b] >=2:
                    if a-block[a][b] <= 0 and b-block[a][b] <= 0:
                        sum += block[0][0]
                        backtrack(i+1)
                    elif a-block[a][b] <=0 and b-block[a][b] > 0:
                        sum += block[0][b-block[a][b]]
                        backtrack(i+1)
                    elif a-block[a][b] > 0 and b-block[a][b] <= 0:
                        sum += block[a-block[a][b]][0]
                        backtrack(i+1)
                    elif a-block[a][b] > 0 and b-block[a][b] > 0:
                        sum += block[a-block[a][b]][b-block[a][b]]
                        backtrack(i+1)


for tc in range(1,1+int(input())):
    n,m,h = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(h)]
    max_sum = -1
    sum = 0
    backtrack()
    print('#{} {}'.format(tc, max_sum))
