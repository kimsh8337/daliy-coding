# 완전검색
# TSP문제는 순열 사용
# TSP는 탐색 후 시작지점으로 돌아와야 하는 것

# 그래프 문제
# 인접 행렬에다가 좌표를 다 받아 넣고, 가중치를 계산해서 넣기
# 메모이제이션 보다는 그래프 형태로 저장해놓고, 가중치값을 그래프에 저장해놓고 쓰면 됨!


import sys
sys.stdin = open('input.txt', 'r')

def tsp(n, pre, total):
    global min_v

    if total > min_v:
        return
    if n == N:
        dis = abs(pre[0] - home[0]) + abs(pre[1] - home[1])
        min_v = min(min_v, total + dis)
        return
    for k in range(N):
        if not visited[k]:
            visited[k] = True
            dis = abs(pre[0] - client[k][0]) + abs(pre[1] - client[k][1])
            tsp(n + 1, client[k], total + dis)
            visited[k] = False

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [*map(int, input().split())]
    com = (arr[0], arr[1])
    home = (arr[2], arr[3])
    client = []
    min_v = 1e10
    for i in range(4, N * 2 + 4, 2):
        client.append((arr[i], arr[i + 1]))

    visited = [False] * N
    tsp(0, com, 0)
    print('#{} {}'.format(tc, min_v))