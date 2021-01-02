import time

start = time.time()

priorities = [1,1,9,1,1,1]
location = 0

def solution(priorities, location):
    stack = []
    answer = 0

    while priorities:
        for i in range(len(priorities)):
            if priorities[i] == max(priorities):
                stack.append(priorities[i])
                priorities[i] = -1
                answer += 1
                if i == location:
                    return answer

print(solution(priorities, location))
print(time.time() - start)