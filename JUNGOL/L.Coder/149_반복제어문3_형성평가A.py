n = int(input())
arr = [[0]*n for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        if num < 10:
            arr[i][j] = num
            num += 2
        else:
            num = 3
            arr[i][j] = 1
for i in range(n):
    for j in range(n):
        print(arr[i][j], end= ' ')
    print()