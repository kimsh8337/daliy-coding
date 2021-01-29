citations = [3, 0, 6, 1, 5]

def solution(citations):
    answer = 0
    h = 1

    while 1:
        cnt = 0
        h += 1
        for i in citations:
            if i >= h:
               cnt += 1
        if h <= cnt and len(citations) - cnt <= h:
            if answer < h:
                answer = h
        else:
            break

    return answer

print(solution(citations))