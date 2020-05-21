import sys
sys.stdin = open('input5247.txt', 'r')
from _collections import deque

for tc in range(1,1+int(input())):
    n, m = map(int, input().split())
    visit = [0]*1000001
    q = deque()

    q.append((n,0))
    visit[n] = 1

    while q:
        cur, dist = q.popleft()
        if cur == m: break
        arr = [cur + 1, cur - 1, cur << 1, cur -10] # cur << 1 == cur *2
        for next in arr:
            if next < 1 or next > 1000000 or visit[next]: continue
            visit[next] = visit[cur] + 1
            if next == m:
                ans = dist + 1
                q.clear()
                break
            q.append((next,dist+1))

    print('#{} {}'.format(tc, ans))



# dfs - 3번째꺼 시간초과
# def dfs(cnt, res):
#     global min_cnt
#     if min_cnt < cnt or res > 1000000 or res < 1:
#         return
#
#     if res == m:
#         min_cnt = min(min_cnt,cnt)
#         return
#
#     dfs(cnt+1, res+1)
#     dfs(cnt+1, res-1)
#     dfs(cnt+1, res*2)
#     dfs(cnt+1, res-10)
#
#
# for tc in range(1,1+int(input())):
#     n,m = map(int, input().split())
#     min_cnt = float('inf')
#     dfs(0, n)
#     print('#{} {}'.format(tc, min_cnt))