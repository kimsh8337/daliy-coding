# import sys; sys.stdin = open('input.txt','r')
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

V = int(input())
E = V+1
arr = list(map(int, input().split()))
L = [0] * (V+1)     # 왼쪽
R = [0] * (V+1)     # 오른쪽
P = [0] * (V+1)     # 부모

for i in range(0,len(arr),2):
    parent, child = arr[i], arr[i+1]
    if L[parent]:
        R[parent] = child
    else:
        L[parent] = child
    P[parent] = parent

def inorder(v): # 방문하는 노드 번호
    if v == 0: return
    # 전위
    inorder(L[v])
    # 중위
    print(v, end=' ')
    inorder(R[v])
    # 후위

inorder(1)
