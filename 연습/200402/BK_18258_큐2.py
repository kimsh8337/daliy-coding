import sys
sys.stdin = open('input.txt', 'r')

queue = []
for _ in range(int(input())):
    a = list(input().split())
    if len(a) > 1:
        x = int(a[1])
    if a[0] == 'push':
        queue.append(x)
    elif a[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)