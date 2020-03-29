def move(dir):
    if dir == 0:
        for i in range(N):
            for j in range(N-1):
                if tile[j][i] == 0:
                    for k in range(j + 1, N):
                        if tile[k][i] != 0:
                            tile[j][i] = tile[k][i]
                            tile[k][i] = 0
                            break
    elif dir == 1:
        for i in range(N):
            for j in range(N - 1, 0, -1):
                if tile[j][i] == 0:
                    for k in range(j - 1, -1, -1):
                        if tile[k][i] != 0:
                            tile[j][i] = tile[k][i]
                            tile[k][i] = 0
                            break
    elif dir == 2:
        for i in range(N):
            for j in range(N-1):
                if tile[i][j] == 0:
                    for k in range(j + 1, N):
                        if tile[i][k] != 0:
                            tile[i][j] = tile[i][k]
                            tile[i][k] = 0
                            break
    else:
        for i in range(N):
            for j in range(N - 1, 0, -1):
                if tile[i][j] == 0:
                    for k in range(j - 1, -1, -1):
                        if tile[i][k] != 0:
                            tile[i][j] = tile[i][k]
                            tile[i][k] = 0
                            break


def plus(dir):
    if dir == 0:
        for i in range(N):
            for j in range(N-1):
                if tile[j][i] != 0:
                    for k in range(j + 1, N):
                        if tile[k][i] != 0:
                            if tile[k][i] == tile[j][i]:
                                tile[j][i] *= 2
                                tile[k][i] = 0
                            break
    elif dir == 1:
        for i in range(N):
            for j in range(N - 1, 0, -1):
                if tile[j][i] != 0:
                    for k in range(j - 1, -1, -1):
                        if tile[k][i] != 0:
                            if tile[k][i] == tile[j][i]:
                                tile[j][i] *= 2
                                tile[k][i] = 0
                            break
    elif dir == 2:
        for i in range(N):
            for j in range(N-1):
                if tile[i][j] != 0:
                    for k in range(j + 1, N):
                        if tile[i][k] != 0:
                            if tile[i][j] == tile[i][k]:
                                tile[i][j] *= 2
                                tile[i][k] = 0
                            break
    else:
        for i in range(N):
            for j in range(N - 1, 0, -1):
                if tile[i][j] != 0:
                    for k in range(j - 1, -1, -1):
                        if tile[i][k] != 0:
                            if tile[i][j] == tile[i][k]:
                                tile[i][j] *= 2
                                tile[i][k] = 0
                            break


d = ['up', 'down', 'left', 'right']
T = int(input())

for tc in range(1, T + 1):
    N, S = input().split()
    N = int(N)
    tile = [list(map(int, input().split())) for _ in range(N)]
    plus(d.index(S))
    move(d.index(S))

    print("#{}".format(tc))

    for i in range(N):
        for j in range(N):
            print(tile[i][j], end=" ")
        print()