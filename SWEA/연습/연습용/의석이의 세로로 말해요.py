import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    word = []
    length = 0
    for i in range(5):
        w = input()
        word.append(w)
        if length < len(word[i]):
            length = len(word[i])
    ans = [[0]*length for _ in range(5)]
    # print(ans)
    print('#{}'.format(tc), end =' ')
    for i in range(5):
        for j in range(len(word[i])):
            ans[i][j] = word[i][j]
    for i in range(length):
        for j in range(5):
            if ans[j][i] != 0:
                print(ans[j][i] , end = '')
    print()