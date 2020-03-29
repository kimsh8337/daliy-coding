import sys
sys.stdin = open('input.txt','r')

n = int(input())
li = []
rank = []
for i in range(n):
    li.append(list(map(int, input().split())))

for i in range(n):
    cnt = 1
    for j in range(n):
        if i != j:
            if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
                cnt += 1
    rank.append(cnt)

for i in range(n):
    print(rank[i],end=' ')