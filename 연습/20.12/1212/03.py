maps = [[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]]
p = 19
r = 6

from itertools import product

def solution(maps, p, r):
    answer = -1
    for pos in product(range(len(maps)), repeat=2):
        print(pos[0],pos[1])
        for i in range(r//2):
            for j in range(r//2):

    return answer

print(solution(maps,p,r))