import sys
sys.stdin = open('input.txt','r')

N = int(input())

numbers = list(map(int, input().split()))

# 버블 정렬
for i in range(N-1):
    # 두개씩 비교하면서 뒤로 보내기
    for j in range(0, N-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

print(numbers[(N-1)//2])