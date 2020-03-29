import sys
sys.stdin = open('input.txt', 'r')

a,b,v = map(int, input().split())
cnt = (v-b)/(a-b)
if cnt % 1 !=0:
    cnt += 1
print(int(cnt))


# 시간초과
# while 1:
#     cnt += 1
#     sum += a
#     if sum == v:
#         break
#     sum -= b
# print(cnt)
