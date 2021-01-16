customer = [[1,1], [2,1], [3,1], [2,0], [2,1]]
# customer = [[2,1], [1,1], [3,1], [1,0], [1,1], [2,0], [2,1]]
K = 2

# def solution(customer,K):
#     answer = []
#     wait = []
#     num = 0
#
#     for i in range(len(customer)):
#         if num < K:
#             if customer[i][1] == 1:
#                 answer.append(customer[i][0])
#                 num += 1
#             elif customer[i][1] == 0:
#                 if customer[i][0] in answer:
#                     answer.remove(customer[i][0])
#                     num -= 1
#                 elif customer[i][0] in wait:
#                     wait.remove(customer[i][0])
#
#         else:
#             if customer[i][1] == 1:
#                 wait.append(customer[i][0])
#             elif customer[i][1] == 0:
#                 if customer[i][0] in answer:
#                     answer.remove(customer[i][0])
#                     num -= 1
#                     if wait:
#                         answer.append(wait[0])
#                         num += 1
#                         wait.remove(wait[0])
#                 elif customer[i][0] in wait:
#                     wait.remove(customer[i][0])
#
#     answer.sort()
#     return answer
#
# print(solution(customer,K))




def solution(customer, K):
    rooms = []
    wait = []
    for i in range(0, len(customer), 2):
        num, check = customer[i], customer[i + 1]
        if check == 1:
            if K > 0:
                K -= 1
                rooms.append(num)
            else:
                wait.append(num)
        else:
            if num in wait:
                wait.remove(num)
            else:
                rooms.remove(num)
                if len(wait):
                    n_num = wait.pop(0)
                    rooms.append(n_num)
                else:
                    K += 1
    return sorted(rooms)

print(solution(customer,K))