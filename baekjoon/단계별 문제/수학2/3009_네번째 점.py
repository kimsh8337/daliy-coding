import sys
sys.stdin = open('input.txt', 'r')

lst = [list(map(int, input().split())) for _ in range(3)]
x = []
y = []
ans_x, ans_y = 0, 0
for i in range(3):
    x.append(lst[i][0])
    y.append(lst[i][1])
for i in range(3):
    cnt_x, cnt_y = 0, 0
    for j in range(3):
        if x[i] == x[j]:
            cnt_x += 1
        if y[i] == y[j]:
            cnt_y += 1
    if cnt_x == 1:
        ans_x = x[i]
    if cnt_y == 1:
        ans_y = y[i]
print(ans_x,ans_y)

# x_ = []
# y_ = []
# for i in range(3):
#         x, y = map(int, input().split())
#         x_.append(x)
#         y_.append(y)
# for i in range(3):
#         if x_.count(x_[i]) == 1:
#                 x = x_[i]
#         if y_.count(y_[i]) == 1:
#                 y = y_[i]
# print(x, y)