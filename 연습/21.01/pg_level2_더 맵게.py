scoville = [1,2,3,9,10,12]
K = 7

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] <= K:
        if len(heap) <= 1:
            answer = -1
            break
        else:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
            answer += 1

    return answer

print(solution(scoville,K))