# office = [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]]
office = [[1,0,0], [0,0,1], [1,0,0]]
k = 2

def solution(office, k):
    answer = 0
    x = len(office)

    for i in range(x-k+1):
        for j in range(x-k+1):
            check = 0
            for a in range(k):
                for b in range(k):
                    if office[i+a][j+b] == 1:
                        check += 1
            if answer < check:
                answer = check

    return answer

print(solution(office,k))