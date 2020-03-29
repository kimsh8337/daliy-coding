import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    line = input()
    stack = []
    for i in range(len(line)):
        if len(stack) == 0:
            stack.append(line[i])
        elif line[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(line[i])

    print('#{} {}'.format(tc, len(stack)))