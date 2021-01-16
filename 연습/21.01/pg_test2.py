# customer = [[1,1], [2,1], [3,1], [2,0], [2,1]]
customer = [[2,1], [1,1], [3,1], [1,0], [1,1], [2,0], [2,1]]
K = 1

def solution(customer,K):
    answer = []
    wait = []
    num = 0

    for i in range(len(customer)):
        if num < K:
            if customer[i][1] == 1:
                answer.append(customer[i][0])
                num += 1
            elif customer[i][1] == 0:
                if customer[i][0] in answer:
                    answer.remove(customer[i][0])
                    num -= 1
                elif customer[i][0] in wait:
                    wait.remove(customer[i][0])

        else:
            if customer[i][1] == 1:
                wait.append(customer[i][0])
            elif customer[i][1] == 0:
                if customer[i][0] in answer:
                    answer.remove(customer[i][0])
                    num -= 1
                    if wait:
                        answer.append(wait[0])
                        num += 1
                        wait.remove(wait[0])
                elif customer[i][0] in wait:
                    wait.remove(customer[i][0])

    answer.sort()
    return answer

print(solution(customer,K))