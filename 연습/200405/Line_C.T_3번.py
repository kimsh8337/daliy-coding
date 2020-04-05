import sys
sys.stdin=open('input.txt','r')

def solution(road, n):
    answer = -1
    for i in range(len(road)-1):
        li = []
        cnt = 0
        for j in range(i,len(road)):
            if road[j] == '1':
                li.append(road[j])
            elif road[j] == '0':
                if cnt < n:
                    li.append(road[j])
                    cnt += 1
                    if len(li) > answer or answer == -1:
                        answer = len(li)
                else:
                    if len(li) > answer or answer == -1:
                        answer = len(li)
                    break

    return answer

print(solution(list(input()),int(input())))