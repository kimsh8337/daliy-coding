import sys
sys.stdin = open('input.txt','r')
from _collections import deque

# 틀렸습니다....
# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited = [0 for _ in range(n+1)]
#     visited[start] = 1
#     while q:
#         d = q.popleft()
#         result.append(d)
#         cnt = [0 for _ in range(n+1)]
#         min_cnt = float('inf')
#         idx = 0
#         for i in range(1,n+1):
#             if visited[i] == 1: continue
#             for j in range(k):
#                 if code[d-1][j] != code[i-1][j]:
#                     cnt[i] += 1
#         for i in range(1,n+1):
#             if cnt[i] != 0:
#                 if min_cnt > cnt[i]:
#                     min_cnt = cnt[i]
#                     idx = i
#         if idx != 0:
#             visited[idx] = 1
#             if idx != b:
#                 q.append(idx)
#             else:
#                 result.append(idx)
#
#
# n, k = map(int, input().split())
# code = [input() for _ in range(n)]
# a, b =map(int, input().split())
# result = []
# bfs(a)
#
# if len(result) < 1:
#     print(-1)
# else:
#     for i in range(len(result)):
#         if i != len(result)-1:
#             print(result[i], end=' ')
#         else:
#             print(result[i],end='')


def s_path():
    while Q:
        node, path = Q.popleft()
        for i in range(N):
            if visit[i]:continue
            cnt = 0
            for k in range(K):
                if bits[node][k] != bits[i][k]:
                    cnt+=1
                if cnt>1:break
            if cnt > 1: continue
            if i == B-1:
                return path+[i]
            Q.append((i,path+[i]))
            visit[i] = 1
    return 0

N, K = map(int, input().split())
bits = [input() for _ in range(N)]
visit = [0]*N
Q = deque()
A, B = map(int, input().split())
Q.append((A-1,[A-1]))
visit[A-1] = 1

answer = s_path()
if answer:
    for i in answer:
        print(i+1, end=' ')
else:
    print(-1)