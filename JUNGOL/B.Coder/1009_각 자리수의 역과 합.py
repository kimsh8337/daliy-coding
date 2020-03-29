import sys
sys.stdin = open('input.txt', 'r')
arr = []
li = []
sum = 0

for i in range(10):
    n = input()
    arr.append(n)
    if n == '0':
        break
for i in range(len(arr)-1):
    for j in range(len(arr[i])):
       li.append(arr[i][j])

for i in range(len(arr[i])//2):
    li[i], li[-i-1] = li[-i-1],li[i]
print(arr)