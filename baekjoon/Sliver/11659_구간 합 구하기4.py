import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sum_li = [0] * (N+1)

for i in range(1,N+1):
    sum_li[i] = sum_li[i-1] + nums[i-1]


for _ in range(M):
    a, b = map(int, input().split())
    print(sum_li[b] - sum_li[a-1])