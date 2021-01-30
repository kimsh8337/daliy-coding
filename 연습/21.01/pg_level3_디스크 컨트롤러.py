jobs = [[0,3], [1,9], [2,6]]

import heapq

def solution(jobs):
    answer = 0
    last = -1
    now = 0
    wait = []
    n = len(jobs)
    cnt = 0

    while cnt < n:
        for job in jobs:
            if last < job[0] <= now:
                answer += (now-job[0])
                heapq.heappush(wait, job[1])
        if len(wait) > 0:
            answer += len(wait) * wait[0]
            last = now
            now += heapq.heappop(wait)
            cnt += 1
        else:
            now += 1
    return answer // n

print(solution(jobs))