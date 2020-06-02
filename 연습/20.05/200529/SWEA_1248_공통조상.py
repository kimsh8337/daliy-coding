def find(x, y):
    while dic[x]:
        visit[dic[x]] = 1
        x = dic[x]
    while 1:
        if visit[dic[y]]: break
        y = dic[y]
    return dic[y]

def find_p(x):
    res = 1
    for i in range(len(parent[x])):
        res += find_p(parent[x][i])
    return res


for tc in range(1, int(input()) + 1):
    v, e, a, b = map(int, input().split())
    dic = {i: 0 for i in range(v + 1)}
    tmp = list(map(int, input().split()))
    visit = [0] * (v + 1)
    parent = [[] for _ in range(v + 1)]
    for i in range(0, len(tmp), 2):
        parent[tmp[i]].append(tmp[i + 1])
        dic[tmp[i + 1]] = tmp[i]
    ans = find(a, b)
    print('#{} {} {}'.format(tc, ans, find_p(ans)))
