import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = []
cnt = 0
for _ in range(n):
    arr.append(input())

for i in range(n):
    check = []
    for j in range(len(arr[i])):
        if arr[i][j] not in check:
            check.append(arr[i][j])
        else:
            if arr[i][j] == arr[i][j-1]:
                continue
            else:
                break
    else:
        cnt += 1

print(cnt)
