import sys
sys.stdin = open('input.txt','r')

score = [int(input()) for _ in range(5)]

for i in range(len(score)):
    if score[i] < 40:
        score[i] = 40

print(int(sum(score)/5))