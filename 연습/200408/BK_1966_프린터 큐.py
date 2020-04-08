import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

for tc in range(1,1+int(input())):
    n,m = map(int, input().split())
    imp = deque(list(map(int,input().split())))
    q = deque(i for i in range(n))

    cnt = 0
    while q:
        if imp[0] == max(imp):
            cnt += 1
            if q[0] == max[q]:
                print(cnt)
                break
            else:
                imp.popleft()
                q.popleft()
        else:
            imp.append(imp.popleft())
            q.append(q.popleft())
