numbers = [2,1,3,4,1]
# numbers = [5,0,2,7]

from itertools import combinations

def solution(numbers):
    answer = []
    new = list(combinations(numbers,2))

    for i in range(len(new)):
        add = new[i][0] + new[i][1]
        if add not in answer:
            answer.append(add)

    answer.sort()

    return answer

print(solution(numbers))