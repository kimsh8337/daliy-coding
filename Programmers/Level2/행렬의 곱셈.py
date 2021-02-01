arr1 = [[1, 2, 3], [4, 5, 6]]
arr2 = [[1, 4], [2, 5], [3, 6]]

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            new = 0
            for a in range(len(arr1[0])):
                new += arr1[i][a] * arr2[a][j]
            temp.append(new)
        answer.append(temp)

    return answer

print(solution(arr1,arr2))