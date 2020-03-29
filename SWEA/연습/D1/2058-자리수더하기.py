# T = int(input())
# num_list = list(map(int, input().split()))
# result = 1
# for i in num_list:
#     result += i
# print(result)

k = int(input())
sum = 0
for i in range(0,4):
    if k <=0:
        break
    j = k%10
    k = int(k/10)
    sum +=j
print(sum)