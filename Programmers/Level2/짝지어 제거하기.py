def solution(s):
    answer = 0
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    if len(stack) == 0: answer = 1

    # 효율성에서 실패..
    # answer = 0
    # temp = s
    # for word in s:
    #     if len(temp) == 0: break
    #     w = word + word
    #     temp = temp.replace(w, '')
    #
    # if len(temp) == 0: answer = 1
    return answer

print(solution('baabaa'))
print(solution('cdcd'))