import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**5)

def find(st):
    global cnt

    visited[st] = 1
    cycle.append(st)
    student = students[st-1]

    if visited[student]:
        if student in cycle:
            cnt += cycle[cycle.index(student):]
            return
    else:
        find(student)


for tc in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    visited = [0] * (n+1)
    cnt = []

    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            find(i)
    print(n - len(cnt))