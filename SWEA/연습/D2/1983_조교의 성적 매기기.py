import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    score = [list(map(int, input().split())) for _ in range(n)]
    r_score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    mid = []
    final = []
    homework = []
    exam_sum = []
    cnt = 0
    for i in range(n):
        mid.append(score[i][0])
        final.append(score[i][1])
        homework.append(score[i][2])
        mid[i] = mid[i] * 0.35
        final[i] = final[i] * 0.45
        homework[i] = homework[i] * 0.2
        exam_sum.append(mid[i] + final[i] + homework[i])
    for i in range(n):
        if exam_sum[k-1] < exam_sum[i]:
            cnt += 1
    cnt = cnt // (n//10)
    print('#{} {}'.format(tc, r_score[cnt]))

