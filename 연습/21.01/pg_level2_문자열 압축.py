s = "abcabcabcabcdededededede"

def solution(s):
    answer = []
    x = len(s)
    num = 1

    while num <= x:
        new = []
        k = 0
        for i in range(0,x,num):
            if k != 0:
                k -= 1
                continue
            cnt = 1
            a = s[i:i+num]
            b = s[i+num:i+(2*num)]
            if a == b:
                for k in range(i+num,x,num):
                    if s[i:i+num] == s[k:k+num]:
                        cnt += 1
                    else:
                        break
                c = str(cnt) + ''.join(a)
                new.append(c)
                k = cnt - 1
            else:
                new.append(a)
        if len(new) > 0:
            new = ''.join(new)
        if answer :
            if len(answer) > len(new):
                answer = new
        else:
            answer = new
        num += 1

    return len(answer)

print(solution(s))