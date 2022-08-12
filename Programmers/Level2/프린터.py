def solution(priorities, location):
    stack = []

    while 1:
        for i in range(len(priorities)):
            if (priorities[i] == max(priorities)):
                stack.append(priorities[i])
                priorities[i] = -1
                if (i == location):
                    return len(stack)

print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1], 0))