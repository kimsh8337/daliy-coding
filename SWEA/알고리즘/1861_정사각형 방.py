import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())
for t in range(1, tc + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    arr = [0] * (N * N + 1)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    max_cnt = -1

    for i in range(N):
        for j in range(N):
            for k in range(4):
                if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:
                    if nums[i + dx[k]][j + dy[k]] - 1 == nums[i][j]:
                        arr[nums[i][j]] = 1
                        break

    for i in range(1, N * N):
        if arr[i] == 1 and arr[i - 1] == 0:
            cnt = 1
            while True:
                if arr[i + cnt] == 1:
                    cnt += 1
                else:
                    break

            if max_cnt < (cnt + 1):
                max_cnt = cnt + 1
                result_num = i

    print(f'#{t} {result_num} {max_cnt}')