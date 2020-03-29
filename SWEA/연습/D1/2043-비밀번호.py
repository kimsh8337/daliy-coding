P, K = map(int, input().split())


cnt = 0
for i in range(P-K+1):
    cnt += 1
print(cnt)