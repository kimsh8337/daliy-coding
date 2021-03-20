def solution(enter, leave):
    answer = [0] * (len(enter))

    for i in range(len(enter)):
        for j in range(i+1,len(enter)):
            if leave.index(enter[i]) > leave.index(enter[j]):
                answer[enter[i]-1] += 1
                answer[enter[j]-1] += 1
            else:
                for k in range(j+1,len(enter)):
                    if leave.index(enter[k]) < leave.index(enter[i]):
                        answer[enter[i]-1] += 1
                        answer[enter[j]-1] += 1

    return answer

print(solution([1,4,2,3], [2,1,3,4]))