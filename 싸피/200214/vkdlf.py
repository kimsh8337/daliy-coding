def miro(x,y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    stack_x = [0, x]
    stack_y = [0, y]
    while 1:
        for i in range(4):
            if arr[x + dx[i]][y + dy[i]] == 3:
                return 1
        for i in range(4):
            if arr[x+dx[i]][y+dy[i]] == 0:
                x = x + dx[i]
                y = y + dy[i]
                stack_x.append(x)
                stack_y.append(y)
                arr[x][y] = 2
                break
        else:
            stack_x.pop()
            stack_y.pop()
            if len(stack_x) != 0:
                x = stack_x[-1]
                y = stack_y[-1]
            else:
                return 0


for TC_count in range(1,11):
    n = input()
    arr = [list(map(int, ' '.join(input()).split())) for _ in range(100)]
    print('#{} {}' .format(TC_count, miro(1,1)))










def miro(arr1,point,direction):

    if arr1[point[0]][point[1]] == 3:
        return 1

    arr[point[0]][point[1]] = 1
    result = 0
    if direction != 1 and point[0] < 99 and arr[point[0] + 1][point[1]] != 1:
        result += miro(arr, [point[0] + 1, point[1]], 0)
    if direction != 0 and point[0] > 0 and arr[point[0] - 1][point[1]] != 1:
        result += miro(arr, [point[0] - 1, point[1]], 1)
    if direction != 3 and point[1] < 99 and arr[point[0]][point[1] - 1] != 1:
        result += miro(arr, [point[0], point[1]-1], 2)
    if direction != 2 and point[1] < 99 and arr[point[0]][point[1] + 1] != 1:
        result += miro(arr, [point[0], point[1] + 1], 3)
    return result


for TC_count in range(1,11):
    n = input()

    arr = [list(map(int, ' '.join(input()).split())) for _ in range(100)]

    print('#{} {}' .format(TC_count, miro(arr,[1,1],-1)))