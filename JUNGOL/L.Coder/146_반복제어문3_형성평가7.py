n = int(input())
arr = [[0]*n for _ in range(n)]
num_chr = 65
num = 0
for i in range(n):
    for j in range(n):
        if i<=j:
            arr[i][j-i] = chr(num_chr)
            num_chr+=1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = num
            num += 1
for i in range(n):
    for j in range(n):
        print(arr[i][j], end= ' ')
    print()
