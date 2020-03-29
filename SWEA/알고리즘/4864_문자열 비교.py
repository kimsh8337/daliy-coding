import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    str1, str2 = input(),input()
    flag = False

    for i in range(len(str1)-1):
        for j in range(len(str2)-1):
            if str1[i] == str2[j]:
                if str1[i+1] == str2[j+1]:
                    flag = True
                else:
                    flag = False

    print('#{}'.format(tc),end=' ')
    if flag:
        print(1)
    else:
        print(0)

