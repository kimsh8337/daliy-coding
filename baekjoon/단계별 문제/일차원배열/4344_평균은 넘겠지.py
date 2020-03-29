c = int(input())
for i in range(c):
    n_score = list(map(int, input().split()))
    # print(n_score)
    sum = 0
    for j in range(1,len(n_score)):
        sum += n_score[j]
    score_avg = sum / n_score[0]
    cnt = 0
    for j in range(1,n_score[0]+1):
        if n_score[j] > score_avg:
            cnt += 1
    avg = cnt / n_score[0]
    print('{:.3%}'.format(avg))