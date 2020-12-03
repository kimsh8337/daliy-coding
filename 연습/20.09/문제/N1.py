m = "bacbbcdc"
k = "abc"


def solution(m,k):
    answer = ''
    arr = []
    check = []

    for i in range(len(m)):
        arr.append(m[i])

    for i in range(len(k)):
        check.append(k[i])


    num = 0
    flag = 0
    while(num < len(k)):
        for i in range(flag, len(arr)):
            if arr[i] == check[num]:
                arr.pop(i)
                break
            else:
                flag += 1
                continue
        num += 1

    answer = ''.join(arr)
    return answer

print(solution(m,k))