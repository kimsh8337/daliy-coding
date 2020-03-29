num = list(map(int, input().split()))

for i in range(1,7):
    cnt = 0
    for j in range(len(num)):
        if num[j] == i:
            cnt += 1
    print('{} : {}'.format(i,cnt))
        