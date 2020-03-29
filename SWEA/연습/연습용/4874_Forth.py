import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    sik = list(map(str, input().split()))
    stack = []

    for i in range(len(sik)):
        if sik[i].isdigit():
            stack.append(int(sik[i]))
        else:
            if sik[i] == '.' and len(stack)==1:
                ans = stack.pop()
                print('#{} {}'.format(tc,ans))
                break
            if len(stack) >= 2:
                if sik[i] == '+':
                    y = stack.pop()
                    x = stack.pop()
                    ans = x+y
                    stack.append(ans)
                elif sik[i] == '*':
                    y = stack.pop()
                    x = stack.pop()
                    ans = x*y
                    stack.append(ans)
                elif sik[i] == '/':
                    y = stack.pop()
                    x = stack.pop()
                    ans = x//y
                    stack.append(ans)
                elif sik[i] == '-':
                    y = stack.pop()
                    x = stack.pop()
                    ans = x-y
                    stack.append(ans)
                elif sik[i] == '.':
                    print('#{} error'.format(tc))
            else:
                print('#{} error'.format(tc,ans))
                break
