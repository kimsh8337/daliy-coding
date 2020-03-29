import sys
sys.stdin = open('input.txt','r')
T = int(input())

for tc in range(1,T+1):
    s = list(map(str, input()))
    # print(s)
    for i in range(len(s)):
        