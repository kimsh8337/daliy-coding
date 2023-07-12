def solution(k, m, score):
    answer = 0

    # 큰 수부터 상자를 몇개 만들 수 있는지 확인
    score = sorted(score, reverse=True)

    idx = 0
    while len(score) - idx >= m:
        answer += min(score[idx:idx+m]) * m
        idx += m

    return answer

# 2번째 방법
# def solution(k, m, score):
#     answer = 0
#
#     # 큰 수부터 상자를 몇개 만들 수 있는지 확인
#     score = sorted(score)
#
#     while len(score) >= m:
#         box = []
#         for i in range(m):
#             box.append(score[-1])
#             score.pop()
#         answer += min(box) * m
#
#     return answer

print(solution(3, 4, [1,2,3,1,2,3,1]))
# print(solution(4, 3, [4,1,2,2,4,4,4,4,1,2,4,2]))