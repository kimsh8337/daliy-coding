scores = [1,3,7,8,10,15]
# scores = [1,2,12,14,15]
k = 3

# from itertools import combinations

def solution(scores, k):
    answer = 0
    minus = []
    pos = []
    num = 0
    for i in range(len(scores)-1):
        minus.append(scores[i+1] - scores[i])

    while(num < k-1):
        pos.append(minus.index(max(minus)))
        minus[minus.index(max(minus))] = 0
        num += 1

    pos.sort()
    st = 0
    for i in range(len(pos)):
        arr = scores[st:pos[i]+1]
        st = pos[i]+1
        answer += max(arr) - min(arr)
    arr = scores[st:]
    answer += max(arr) - min(arr)



    # for pos in combinations(range(1,len(scores)), k-1):
    #     st = 0
    #     sum = 0
    #     for i in pos:
    #         if sum > answer and answer > 0:
    #             break
    #         arr = scores[st:i]
    #         st = i
    #         sum += max(arr) - min(arr)
    #     if sum < answer or answer == -1:
    #         arr = scores[st:]
    #         sum += max(arr) - min(arr)
    #     if answer < 0 or answer > sum:
    #         answer = sum

    return answer

print(solution(scores,k))