import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import heapq

heap =[]

for _ in range(int(input())):
    x = int(input())

    if x == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)