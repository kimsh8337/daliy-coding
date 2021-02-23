import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    now = list(map(str, input().split()))
    if now[0] == 'push':
        stack.append(int(now[1]))
    elif now[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif now[0] == 'size':
        print(len(stack))
    elif now[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif now[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)