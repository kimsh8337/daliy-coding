import sys
sys.stdin = open('input2.txt', 'r')

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]
print(edges)