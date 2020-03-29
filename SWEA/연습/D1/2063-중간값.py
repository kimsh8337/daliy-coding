N = int(input())

num = list(map(int, input().split()))
num.sort()
print(num[len(num)/2])

# T = int(input())

# lst = list(map(int, input().split()))
# lst.sort()
# print(lst[int((T-1)/2)])