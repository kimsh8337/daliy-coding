import sys
sys.stdin = open('input.txt', 'r')

# 내가 짠 코드
T=int(input())

for tc in range(1, T+1):
    word_list = []
    max_len = 0
    for i in range(5):
        word = input()
        word_list.append(word)
        if max_len < len(word_list[i]):
            max_len = len(word_list[i])
    arr = [[0] * max_len for _ in range(5)]
    for i in range(5):
        for j in range(len(word_list[i])):
            arr[i][j] = word_list[i][j]
    print('#{}'.format(tc),end=' ')
    for i in range(max_len):
        for j in range(5):
            if arr[j][i]:
                print(arr[j][i], end='')
    print()
#
# T = int(input())
#
# for tc in range(1, T+1):
#     words = [0] * 5
#     maxlen =0
#     for i in range(5):
#         words[i] = list(input())
#         if len(words[i]) > maxlen:
#             maxlen = len(words[i])
#
#     print('#{}'.format(tc), end = ' ')
#     for i in range(maxlen):
#         for j in range(5):
#             if len(words[j]) > i:
#                 print(words[j][i], end = '')
#     print()