S = "baaaa"

def solution(S):
    answer = 0
    flag = 2
    for i in range(len(S)):
        if S[i] == 'a':
            flag -= 1
            if flag < 0:
                return -1
        else:
            answer += flag
            flag = 2
    if S[-1] != 'a':
        answer += 2

    return answer

print(solution(S))