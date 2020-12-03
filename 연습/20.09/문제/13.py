A = [6,2,3,5,6,3]

def solution(A):
    answer = 0
    A.sort()
    for i in range(len(A)):
        if answer >= 1000000000:
            answer = -1
            break
        if A[i] != i+1:
            if A[i] > i+1:
                while(1):
                    if A[i] == i+1:
                        break
                    A[i] -= 1
                    answer += 1
            elif A[i] < i+1:
                while(1):
                    if A[i] == i+1:
                        break
                    A[i] += 1
                    answer += 1

    return answer

print(solution(A))