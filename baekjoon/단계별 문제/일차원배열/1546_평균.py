T = int(input())
sum = 0
a = list(map(int, input().split()))

m = max(a)
for i in range(len(a)):
    sum += a[i]/m*100
print(sum/len(a))
