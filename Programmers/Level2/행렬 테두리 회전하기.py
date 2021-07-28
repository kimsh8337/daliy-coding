def solution(rows, columns, queries):
    answer = []
    arr = [[0]*(columns+1) for _ in range(rows+1)]
    num = 1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            arr[i][j] = num
            num += 1

    for query in queries:
        nums = []
        x1,y1,x2,y2 = query[0], query[1], query[2], query[3]

        temp = arr[x1][y1]
        for y in range(y1+1, y2+1):
            nums.append(temp)
            arr[x1][y], temp = temp, arr[x1][y]

        for x in range(x1+1,x2+1):
            nums.append(temp)
            arr[x][y2], temp = temp, arr[x][y2]

        for my in range(y2-1, y1-1, -1):
            nums.append(temp)
            arr[x2][my], temp = temp, arr[x2][my]

        for mx in range(x2-1, x1-1, -1):
            nums.append(temp)
            arr[mx][y1], temp = temp, arr[mx][y1]
        nums.append(temp)
        answer.append(min(nums))

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))