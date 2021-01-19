progresses = [95, 90, 99, 99, 80, 99]
speeds = [1,1,1,1,1,1]

def solution(progresses, speeds):
    answer = []
    x = len(progresses)
    pos = 0
    while 1:
        if pos == x:
            break
        num = 0
        for i in range(pos,x):
            if i == pos:
                if progresses[i] >= 100:
                    num += 1
                    pos += 1
            if progresses[i] < 100:
                progresses[i] += speeds[i]
        if num != 0:
            answer.append(num)
    return answer

print(solution(progresses, speeds))