def check_rules(cmd, rules, pos):
    # pos의 길이가 1보다 작으면 flag_rules에 해당하는 규칙 없음
    if len(pos) > 1:
        # 각각 사용 횟수를 세주기 위해서
        cnt = [0] * 4
        for i in range(len(pos)-1):
            cmd_type = cmd[pos[i]]
            # NULL일 경우 value값이 없음
            if rules.get(cmd_type) == 'NULL':
                continue
            else:
                if len(rules.get(cmd_type)[1]) > 1:
                    if rules.get(cmd_type)[0] == 'NUMBER':
                        cnt[0] += 1
                        # 현 cmd_type 다음 위치부터 다음 cmd_type이 나오기 전까지의 값을 넣음
                        cmd_value = []
                        for j in range(pos[i] + 1, pos[i + 1]):
                            cmd_value.append(cmd[j])
                        # 길이가 1보다 크면 False
                        if len(cmd_value) > 1:
                            return False
                        for num in cmd_value:
                            if not num.isnumeric():
                                return False
                    elif rules.get(cmd_type)[0] == 'STRING':
                        cnt[1] += 1
                        # 현 cmd_type 다음 위치부터 다음 cmd_type이 나오기 전까지의 값을 넣음
                        cmd_value = []
                        for j in range(pos[i] + 1, pos[i + 1]):
                            cmd_value.append(cmd[j])
                        # 길이가 1보다 크면 False
                        if len(cmd_value) > 1:
                            return False
                        for s in cmd_value:
                            if not s.isalpha():
                                return False
                    elif rules.get(cmd_type)[0] == 'NUMBERS':
                        cnt[2] += 1
                        # 현 cmd_type 다음 위치부터 다음 cmd_type이 나오기 전까지의 값을 넣음
                        cmd_value = []
                        for j in range(pos[i] + 1, pos[i + 1]):
                            cmd_value.append(cmd[j])
                        # 길이가 1이상이어야 하기 때문에 작으면 False
                        if len(cmd_value) < 1:
                            return False
                        for value in cmd_value:
                            for num in value:
                                if not num.isnumeric():
                                    return False
                    elif rules.get(cmd_type)[0] == 'STRINGS':
                        cnt[3] += 1
                        # 현 cmd_type 다음 위치부터 다음 cmd_type이 나오기 전까지의 값을 넣음
                        cmd_value = []
                        for j in range(pos[i] + 1, pos[i + 1]):
                            cmd_value.append(cmd[j])
                        # 길이가 1이상이어야 하기 때문에 작으면 False
                        if len(cmd_value) < 1:
                            return False
                        for value in cmd_value:
                            for s in value:
                                if not s.isalpha():
                                    return False
                else:
                    # rules 규칙에 맞는지 확인
                    if rules.get(cmd_type) == 'NUMBER':
                        cnt[0] += 1
                        # 현 cmd_type 다음 위치부터 다음 cmd_type이 나오기 전까지의 값을 넣음
                        cmd_value = []
                        for j in range(pos[i] + 1, pos[i + 1]):
                            cmd_value.append(cmd[j])
                        # 길이가 1보다 크면 False
                        if len(cmd_value) > 1:
                            return False
                        for num in cmd_value:
                            if not num.isnumeric():
                                return False
                    elif rules.get(cmd_type) == 'STRING':
                        cnt[1] += 1
                        # 현 cmd_type 다음 위치부터 다음 cmd_type이 나오기 전까지의 값을 넣음
                        cmd_value = []
                        for j in range(pos[i] + 1, pos[i + 1]):
                            cmd_value.append(cmd[j])
                        # 길이가 1보다 크면 False
                        if len(cmd_value) > 1:
                            return False
                        for s in cmd_value:
                            if not s.isalpha():
                                return False
                    elif rules.get(cmd_type) == 'NUMBERS':
                        cnt[2] += 1
                        # 현 cmd_type 다음 위치부터 다음 cmd_type이 나오기 전까지의 값을 넣음
                        cmd_value = []
                        for j in range(pos[i]+1,pos[i+1]):
                            cmd_value.append(cmd[j])
                        # 길이가 1이상이어야 하기 때문에 작으면 False
                        if len(cmd_value) < 1:
                            return False
                        for value in cmd_value:
                            for num in value:
                                if not num.isnumeric():
                                    return False
                    elif rules.get(cmd_type) == 'STRINGS':
                        if cnt[3] >= 1:
                            return False
                        # 현 cmd_type 다음 위치부터 다음 cmd_type이 나오기 전까지의 값을 넣음
                        cmd_value = []
                        for j in range(pos[i]+1,pos[i+1]):
                            cmd_value.append(cmd[j])
                        # 길이가 1이상이어야 하기 때문에 작으면 False
                        if len(cmd_value) < 1:
                            return False
                        for value in cmd_value:
                            for s in value:
                                if not s.isalpha():
                                    return False


    else:
        return False
    if max(cnt) > 1:
        return False
    return True


def check_idx(cmd,rules):
    pos = []

    for c in cmd:
        if c in rules:
            pos.append(cmd.index(c))
    pos.append(len(cmd))  # cmd의 끝 길이를 알기 위해서

    return pos


def check_name(name, cmd_name):
    if name == cmd_name:
        return True
    else:
        return False


def solution(program, flag_rules, commands):
    answer = []
    rules = dict()
    # ALIAS가 나오는 부분을 제일 뒤로 보내기위해서
    flag_rules.sort(key=len)

    # 주어진 rules을 확인하기 위해 rules라는 딕셔너리를 만든다.
    for rule in flag_rules:
        if len(rule.split()) == 2:
            flag_name, flag_type = rule.split()
            rules[flag_name] = flag_type
        if len(rule.split()) == 3:
            flag_name, bold, flag_type = rule.split()
            rules[flag_name] = rules.get(flag_type),bold

    for command in commands:
        cmd = command.split()

        # 실행할 프로그램 이름과 command에서 입력하는 프로그램 이름이 같은지 확인
        flag = check_name(program,cmd[0])

        # flag가 True일 경우에만 cmd 체크
        if flag:
            # cmd name의 위치를 미리 확인
            pos = check_idx(cmd[1:],rules)
            # flag_rules의 규칙에 맞는지 확인
            flag = check_rules(cmd[1:],rules,pos)
        answer.append(flag)

    return answer

print(solution("line",["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"],["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
print(solution("bank",["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"],["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))