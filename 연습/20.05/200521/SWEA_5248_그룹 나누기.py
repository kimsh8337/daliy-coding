import sys
sys.stdin = open('input5248.txt', 'r')


def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


def union(x,y):
    parent[find_set(y)] = find_set(x)


for tc in range(1, 1+int(input())):
    n, m = map(int, input().split())
    parent = [0]*(n+1)

    for i in range(1, n+1):
        parent[i] = i

    data = list(map(int, input().split()))
    for i in range(m):
        st = data[2*i]
        ed = data[2*i+1]
        union(st, ed)

    result = []
    for i in range(len(parent)):
        result.append(find_set(i))

    print('#{} {}'.format(tc, len(set(result))-1))