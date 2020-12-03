N = 14

def multi(ans):
    mul = 1
    for j in range(len(ans)):
        if int(ans[j]) == 0:
            continue
        else:
            mul *= int(ans[j])
    return mul


def solution(N):
    answer = []
    maxnum = 0
    maxmul = 0
    for i in range(2, N):
        num = 0
        che = N
        ans = ""
        while (1):
            if che >= i:
                a = che % i
                che = che // i
                ans = str(a) + ans
                num += 1
            else:
                ans = str(che) + ans
                # print(ans)
                break
        mul = multi(ans)
        if maxmul <= mul:
            maxnum = i
            maxmul = mul
    answer.append(maxnum)
    answer.append(maxmul)

    return answer

print(solution(N))