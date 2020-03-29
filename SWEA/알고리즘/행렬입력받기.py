# import sys
# sys.stdin = open('input.txt' , 'r')

# a, b = map(int, input().split())

# for i in range(a):
#     a_list = list(map(int, input().split()))
#     print(a_list)


# R, C = map(int, (input().split())
# 1. 행의 크기를 정해놓고 인덱스로 접근하여 넣기
# arr = [0] * R
# for i in range(R):
#     arr[i] = list(map(int, input().split()))
#     print(arr[i])

# 2. append() 내장함수를 써서 리스트에 집어넣기
# arr = []
# for i in range(R):
#     arr.append(list(map(int, input().split())))
#     print(arr[i])

# 3. 리스트 내포를 써서 직접선언
# arr = [list(map(int, input().split())) for _ in range(R)]
# for i in range(R):
#     print(arr[i]) 

arr = [3][4]
for i in range(4):
    arr[i] = list(map(int, input()))
    print(arr[i])