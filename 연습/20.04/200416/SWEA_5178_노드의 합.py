import sys
sys.stdin = open('input.txt','r')

def find(node):
    global sum
    if node*2 > n:
        sum += tree[node]
    else:
        find(node*2)
        if node*2 != n:
            find(node*2+1)

for tc in range(1, int(input()) + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)
    sum = 0
    for _ in range(m):
        i, v = map(int, input().split())
        tree[i] = v
    find(l)
    print('#{} {}'.format(tc,sum))