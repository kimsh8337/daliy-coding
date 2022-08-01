cnt = 0

def checkWire(wires, num, check):
    global cnt
    for i in range(len(wires)):
        if wires[i][0] == num and check[i] != 1:
            check[i] = 1
            cnt += 1
            checkWire(wires, wires[i][1], check)
        if wires[i][1] == num and check[i] != 1:
            check[i] = 1
            cnt += 1
            checkWire(wires, wires[i][0], check)
    return

def solution(n, wires):
    global cnt
    answer = -1
    for i in range(n - 1):
        temp = []
        for j in range(n - 1):
            if i != j: temp.append(wires[j])
        check = [0] * (n - 1)
        cnt = 1
        checkWire(temp, temp[0][0], check)
        if answer == -1 or answer > abs((n - cnt) - cnt):
            answer = abs(abs(n - cnt) - cnt)

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))