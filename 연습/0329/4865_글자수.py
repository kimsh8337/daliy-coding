import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,1+int(input())):
    str1 = input()
    str2 = input()
    li = [0] * len(str1)

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                li[i] += 1

    print('#{} {}'.format(tc, max(li)))