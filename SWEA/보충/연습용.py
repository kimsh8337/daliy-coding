# 연속한 1의 개수
# 테스트 케이스는
# 첫줄에 테스트 케이스 개수
# 테스트 케이스의 첫 번째 줄에는 문자열의 길이 n
# 두 번재 줄에는 길이 n인 0과 1로 이루어진 문자열

# 내가 짠 코드
# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#     lst = list(map(int, input()))
#
#     cnt = 0
#     res = 0
#     for i in range(len(lst)):
#         if lst[i] == 1:
#             cnt += 1
#             if res < cnt:
#                 res = cnt
#         else:
#             cnt = 0
#     print('#{} {}'.format(tc, res))

# 해설
T = int(input())  # 정수형태 문자열 읽어서 정수로 변환
for tc in range(1, T+1):
    n = int(input())
    numbers = input()   # 0011001110
    max_one = 0   # 제일 긴 1의 연속을 저장할 변수
    count = 0   # 현재 연속된 1의 길이를 저장할 변수
    for i in range(len(numbers)):
        # 만약에 현재 요소가 1이면 count 1 증가
        if numbers[i] == '1':
            count += 1
        # 0이면 max와 비교해서 더 크면 max에 count 저장
        else:
            if max_one < count :
                max_one = count
        # count를 0으로 만들어준다.
            count = 0
    if max_one < count:
        max_one = count
    print('#{} {}'.format(tc, max_one))
