import sys
sys.stdin = open('input.txt', 'r')

a = int(input())
i = 0
while a > 0:
    a -= i
    i += 1

a = i+a-1
res = str(a) + '/' + str(i-a)
if i % 2 == 0:
    res = str(i-a) + '/' + str(a)

print(res)



# 시간초과
# k = int(input())
#
# a = 1
# b = 1
# ab_flags = True
#
# if k == 1:
#     print('1/1')
#
# for _ in range(k-1):
#     if ab_flags:
#         if a == 1:
#             ab_flags = False
#         else:
#             a -= 1
#         b+=1
#     else:
#         if b == 1:
#             ab_flags = True
#         else:
#             b -= 1
#         a+= 1
# print('{}/{}'.format(a,b))



