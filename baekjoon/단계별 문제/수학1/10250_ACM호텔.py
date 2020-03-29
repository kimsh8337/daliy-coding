import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    num = 1
    h,w,n = map(int, input().split())
    hotel = [[0]*w for _ in range(h)]

    for i in range(w):
        for j in range(-1,-h-1,-1):
            hotel[j][i] = num
            num += 1
            if hotel[j][i] == n:
                ans = (-j)*100+i+1
                break
    print(ans)
