S = ["zzzz","ferz","zdsr","fgtd"]

def solution(S):
    answer = []
    n = len(S[0])
    m = len(S)
    for k in range(m):
        if len(answer) > 0:
            break
        for i in range(n):
            if len(answer) > 0:
                break
            num = i
            while(1):
                if num > m-2 or len(answer) > 0:
                    break
                for j in range(n):
                    if S[i][j] == S[num+1][j]:
                        a = i
                        b = num+1
                        c = j
                        answer.append(a)
                        answer.append(b)
                        answer.append(c)
                        break
                num += 1

    return answer

print(solution(S))