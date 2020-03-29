import sys
sys.stdin = open('input.txt','r')

for tc in range(1, 1+int(input())):
    arr = list(input())
    stack = []
    flag = True

    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] =='{':
            stack.append(arr[i])
        if arr[i] == '}' or arr[i] == ')':
            if len(stack) == 0:
                flag = False
                break
            else:
                if (arr[i]==')' and stack[-1] != '(') or (arr[i]=='}' and stack[-1] != '{'):
                    flag = False
                    break
                else:
                    flag = True
                    stack.pop()

    print('#{}'.format(tc), end = ' ')
    if flag and len(stack)==0:
        print(1)
    else:
        print(0)