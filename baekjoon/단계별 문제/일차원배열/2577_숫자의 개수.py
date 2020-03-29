a = int(input())
b = int(input())
c = int(input())
x = str(a*b*c)
arr = list(map(int, x))
for i in range(10):
    cnt = 0
    for j in range(len(arr)):
        if i == arr[j]:
            cnt += 1
    print(cnt)