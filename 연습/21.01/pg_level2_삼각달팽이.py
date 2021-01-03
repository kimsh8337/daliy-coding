n =6

def solution(n):
    answer = []
    num = 1
    arr = [[0] * n for _ in range(n)]
    a,b = -1,0

    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                a += 1
            elif i % 3 == 1:
                b += 1
            elif i % 3 == 2:
                a -= 1
                b -= 1
            arr[a][b] = num
            num += 1

    for i in arr:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer

print(solution(n))