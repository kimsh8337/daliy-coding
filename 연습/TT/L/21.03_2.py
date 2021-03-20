def solution(inp_str):
    ans, res, con = [], {}, set()
    spec = ['~', '!', '@', '#', '$','%','^','&','*']
    E_cnt, e_cnt, num = 1, 1, 1

    if len(inp_str) < 8 or len(inp_str) > 15:
        ans.append(1)

    for s in inp_str:
        if s not in res:
            res[s] = 1
        else:
            res[s] = res.get(s)+1

        if s.isnumeric():
            con.add('number')
            if 4 not in ans:
                for i in range(inp_str.index(s)+1, len(inp_str)):
                    if inp_str[i] == s:
                        num += 1
                    else:
                        break
                if num >= 4:
                    ans.append(4)
                num = 0


        if not s.isalpha() and not s.isnumeric():
            if s not in spec:
                if 2 not in ans:
                    ans.append(2)
            else:
                con.add('spec')

        if s.isalpha() and s.isupper():
            con.add('upper')
            if 4 not in ans:
                for i in range(inp_str.index(s)+1,len(inp_str)):
                    if inp_str[i]==s:
                        E_cnt += 1
                    else:
                        break
                if E_cnt >= 4:
                    ans.append(4)
                E_cnt = 0

        if s.isalpha() and s.islower():
            con.add('lower')
            if 4 not in ans:
                for i in range(inp_str.index(s)+1,len(inp_str)):
                    if inp_str[i] == s:
                        e_cnt += 1
                    else:
                        break
                if e_cnt >= 4:
                    ans.append(4)
                e_cnt = 0

    if max(res.values()) >= 5:
        ans.append(5)

    if len(con) < 3:
        ans.append(3)

    if ans:
        ans.sort()
    else:
        return [0]

    return ans

# print(solution("AaTa+!12-3"))
print(solution("ZzZz9Z824"))