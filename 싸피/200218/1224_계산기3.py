import sys
sys.stdin = open('input.txt','r')


for tc in range(1,11):
    n = int(input())
    s = list(map(str, input()))
    sik = []
    stack = []
    for i in range(n):
        if s[i].isdigit():
            sik.append(s[i])
        elif s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            for j in range(len(stack)):
                if stack[-1] != '(':
                    sik.append(stack[-1])
                    stack.pop()
                elif stack[-1] == '(':
                    stack.pop()
                    break
        elif s[i] == '*':
            if stack[-1] == '*':
                sik.append(s[i])
            else:
                stack.append(s[i])
        elif s[i] == '+':
            if stack[-1] == '*':
                sik.append(stack[-1])
                stack.pop()
                stack.append(s[i])
            elif stack[-1] == '+':
                sik.append(s[i])
            else:
                stack.append(s[i])
    for i in range(len(sik)):
        if sik[i].isdigit():
            stack.append(int(sik[i]))
        else:
            if sik[i] == '+':
                x = stack.pop()
                y = stack.pop()
                ans = y + x
                stack.append(ans)
            elif sik[i] == '*':
                x = stack.pop()
                y = stack.pop()
                ans = y * x
                stack.append(ans)

    print('#{} {}'.format(tc, stack[-1]))