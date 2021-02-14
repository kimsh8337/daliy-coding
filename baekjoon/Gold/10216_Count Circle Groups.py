import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(a):
    if a == parents[a]:
        return a
    else:
        b = find(parents[a])
        parents[a] = b
        return b

def merge(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    parents[b] = a
    return True

for tc in range(int(input())):
    n = int(input())
    area = []
    parents = [0] * n
    for i in range(n):
        x, y, r = map(int, input().split())
        area.append((x,y,r))
        parents[i] = i

    for i in range(n):
        for j in range(i+1,n):
            x1 = area[i][0]
            x2 = area[j][0]
            y1 = area[i][1]
            y2 = area[j][1]
            dis = area[i][2] + area[j][2]

            if (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) <= dis * dis :
                merge(i,j)

    for i in range(n):
        parents[i] = find(i)

    print(len(set(parents)))