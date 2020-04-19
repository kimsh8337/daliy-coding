import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    n,m = map(int,input().split())
    ls = list(map(int,input().split()))
    num = []
    for i in ls:
        num.append(i)
    result = [0]*n
    q = [i for i in range(n)]
    sequence = 1
    while q:
        if ls[q[0]] == max(num):
            num.remove(max(num))
            result[q.pop(0)] = sequence
            sequence += 1
        else:
            q.append(q.pop(0))
    print(result[m])
