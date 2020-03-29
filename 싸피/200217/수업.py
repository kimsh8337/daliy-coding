# 재귀 함수
# 재귀 호출은 반복을 한다.
# 함수 호출을 종료해야 한다.

# for i in range(3):  # 0,1,2
#     print('Hello!!!')

# path = []
# def printhello(i,n):
#
#     if i == n :
#         print(path)
#     else:
#         path.append(1)
#         printhello(i+1,n)
#         path.pop()
#
#         path.append(0)
#         printhello(i+1,n)
#         path.pop()
#
# printhello(0,3)

# n = 3
# bit = [0]*n
# for i in range(2):
#     bit[0] = i
#     for i in range(2):
#         bit[1] = i
#         for i in range(2):
#             bit[2] = i
#             print(bit)

# n = 3
# bit = [0]*n
# def subset(k,n):
#     if k ==n:
#         print(bit)
#     else:
#         for i in range(2):
#             bit[k] = i
#             subset(k+1,n)
# subset(0,n)