r,c = map(int,input().split())
arr = [[0]*c for _ in range(r)]

for i in range(r):
    num = 0
    for j in range(c):
        num += i+1
        arr[i][j] = num
for i in range(r):
    for j in range(c):
        print(arr[i][j], end = ' ')
    print()