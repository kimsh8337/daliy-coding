import sys
sys.stdin=open('input.txt','r')
from _collections import deque
n = int(sys.stdin.readline())
Q = deque()
for i in range(n):
    order = sys.stdin.readline().split()
    if order[0]=='push':
        Q.append(int(order[1]))
    elif order[0] == 'pop':
        if len(Q)!=0:
            print(Q.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(Q))
    elif order[0] == 'empty':
        if not Q:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(Q)!=0:
            print(Q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(Q)!=0:
            print(Q[-1])
        else:
            print(-1)