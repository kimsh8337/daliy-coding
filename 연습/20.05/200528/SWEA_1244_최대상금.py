import sys
sys.stdin = open("input.txt", "r")
from collections import deque
d = [1, 10, 100, 1000, 10000, 100000]

for tc in range(1, int(input()) + 1):
    num, cnt = map(str, input().split())
    N = len(num)
    cnt = int(cnt)
    ans = 0
    visit = [set() for _ in range(cnt + 1)]

    Q = deque()
    Q.append((int(num), 0))

    while Q:
        val, k = Q.popleft()
        if k == cnt:
            ans = max(ans, val)
        else:
            for i in range(N - 1):
                for j in range(i + 1, N):
                    # i, j번 위치의 해당하는 값을 추출
                    a = (val // d[i]) % 10
                    b = (val // d[j]) % 10
                    t = val - a * d[i] + b * d[i] - b * d[j] + a * d[j]
                    if t in visit[k + 1]:
                        continue
                    visit[k + 1].add(t)
                    Q.append((t, k + 1))

    print('#{} {}'.format(tc, ans))