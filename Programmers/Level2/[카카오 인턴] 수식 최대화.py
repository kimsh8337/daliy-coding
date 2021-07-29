from itertools import permutations

def operation(num1, num2, op):
    if op == "+":
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def calculate(exp, op):
    arr = []
    tmp = ""
    for i in exp:
        if i.isdigit() == True:
            tmp += i
        else:
            arr.append(tmp)
            arr.append(i)
            tmp = ""
    arr.append(tmp)

    for o in op:
        stack = []
        while len(arr) != 0:
            tmp=arr.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(), arr.pop(0), o))
            else:
                stack.append(tmp)
        arr = stack

    return abs(int(arr[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    res = []

    for i in op:
        res.append(calculate(expression,i))
    return max(res)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))