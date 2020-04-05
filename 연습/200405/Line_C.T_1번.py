import sys
sys.stdin = open('input.txt','r')

def solution(inputString):
    op = ['(', '{', '[', '<']
    cl = [')', '}', ']', '>']
    li = []
    answer = 0

    for i in range(len(inputString)):
        if inputString[i] in op:
            li.append(inputString[i])
        elif inputString[i] in cl:
            if len(li) != 0:
                li.pop()
                answer += 1
            else:
                answer = -1
    if len(li) != 0:
        answer = -1
    return answer

print(solution(list(input())))