import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    code = list(map(str, input().split()))
    stack = []
    # print(code)
    for i in range(len(code)):
        if code[i].isdigit():
            stack.append(code[i])
        else:
            if len(stack) >= 2:
                if code[i] == '+':
                    x = int(stack.pop())
                    y = int(stack.pop())
                    ans = y + x
                    stack.append(ans)
                elif code[i] == '-':
                    x = int(stack.pop())
                    y = int(stack.pop())
                    ans = y - x
                    stack.append(ans)
                elif code[i] == '*':
                    x = int(stack.pop())
                    y = int(stack.pop())
                    ans = y * x
                    stack.append(ans)
                elif code[i] == '/':
                    x = int(stack.pop())
                    y = int(stack.pop())
                    ans = y // x
                    stack.append(ans)
                elif code[i] == '.':
                    print('#{} error'.format(tc))
                    break
            else:
                if code[i] in '+-*/':
                    print('#{} error'.format(tc))
                    break
                else:
                    print('#{} {}'.format(tc, stack[-1]))
                    break
