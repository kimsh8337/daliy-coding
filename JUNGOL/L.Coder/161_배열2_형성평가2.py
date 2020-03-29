import sys
sys.stdin = open('input.txt','r')

score = list(map(int, input().split()))

for i in range(110,-1,-10):
    cnt = 0
    for j in range(len(score)):
        if score[j] != 0:
            if i-10<=score[j]<i:
                cnt += 1
        else:
            break
    if cnt != 0:
        print('{} : {} person'.format(i-10,cnt))
