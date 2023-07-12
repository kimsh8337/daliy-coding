def solution(answers):
    answer = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result_num1 = 0
    result_num2 = 0
    result_num3 = 0

    for i in range(0, len(answers), 5):
        for j in range(i, 5 + i):
            if j == len(answers):
                break
            if answers[j] == num1[j % 5]:
                result_num1 += 1

    for i in range(0, len(answers), 8):
        for j in range(i, 8 + i):
            if j == len(answers):
                break
            if answers[j] == num2[j % 8]:
                result_num2 += 1

    for i in range(0, len(answers), 10):
        for j in range(i, 10 + i):
            if j == len(answers):
                break
            if answers[j] == num3[j % 10]:
                result_num3 += 1
    
    max_score = max(result_num1, result_num2, result_num3)

    if (max_score == result_num1):
        answer.append(1)
    if (max_score == result_num2):
        answer.append(2)
    if (max_score == result_num3):
        answer.append(3)

    return answer

print(solution([1,2,3,4,5]))