n = 4

from itertools import combinations

def solution(n):
    answer = []
    new = []
    num = 0

    for i in range(n):
        new.append(i)
    print(list(combinations(new,n-1)))

    # while num < n-1:



    return answer

print(solution(n))