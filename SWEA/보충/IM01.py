# IM 배열을 얼마나 잘 순회 할 수 있는가?
# 배열? 변수 여러개 선언하는 것이다.
# 각각의 변수는 인덱스를 이용해서 접근한다.
arr = [1, 2, 3, 4, 5]  # 배열의 길이 5
arr[0] = 7
# 배열의 모든 인덱스에 접근하는 방법
for i in range(len(arr)):    # for 반복문 반복횟수 정해져있을때 사용
    print(i, end=' ')
print()
# 접근하고자 하는 인덱스 설정방법
for i in range(1,len(arr)-1): # 시작 인덱스, 종료 인덱스(미포함)
    print(arr[i], end= ' ')
print()

for i in range(1,len(arr)-1,2): # 시작 인덱스, 종료 인덱스(미포함)
    print(arr[i], end= ' ')
print()

for i in range(0,len(arr),1):
    print(i, end=' ')
print()

# 마지막 인덱스부터 0번 인데스까지 접근하기
for i in range(len(arr)-1, -1, -1):
    # print(i, end=' ')
    print(arr[i], end= ' ')
print()

