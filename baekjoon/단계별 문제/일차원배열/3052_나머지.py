arr = []
for i in range(10):
    a = int(input())
    c = a%42
    arr.append(c)
print(len(set(arr)))
