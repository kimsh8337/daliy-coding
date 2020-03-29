import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    s = list(map(str, input()))
    for i in range(1):
        cnt = 1
        for j in range(i+1,len(s)):
            if s[i] != s[j]:
                cnt += 1
            if s[i] == s[j]:
                if s[i+1] == s[j+1]:
                    break
                else:
                    cnt += 1

    print('#{} {}'.format(tc, cnt))
