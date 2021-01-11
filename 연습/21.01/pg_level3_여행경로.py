# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
tickets = [["ICN","AAA"], ["ICN","BBB"], ["BBB","ICN"]]

from collections import deque

def solution(tickets):
    answer = []
    path = ["ICN"]
    visited = [0] * len(tickets)
    new = []
    Q = deque()


    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            new.append(tickets[i][1])
    new.sort()

    for i in range(len(new)):
        for j in range(len(tickets)):
            if 0 in visited:
                visited = [0] * len(tickets)
                path = ["ICN"]
            else:
                answer = path
                break
            if new[i] == tickets[j][1] and tickets[j][0] == "ICN":
                Q.append((tickets[j][0], tickets[j][1]))

                while Q:
                    check = []
                    st, ed = Q.popleft()
                    path.append(ed)

                    for k in range(len(tickets)):
                        if tickets[k][0] == st and tickets[k][1] == ed:
                            visited[k] = 1
                            break

                    if not 0 in visited:
                        break

                    for k in range(len(tickets)):
                        if tickets[k][0] == ed and visited[k] == 0:
                            check.append(tickets[k][1])
                    if check:
                        check.sort()
                    else:
                        break

                    for j in range(len(tickets)):
                        if check[0] == tickets[j][1] and tickets[j][0] == ed:
                            Q.append((tickets[j][0], tickets[j][1]))
                            break

    return answer
print(solution(tickets))