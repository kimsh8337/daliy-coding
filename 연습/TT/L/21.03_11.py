def check_rules(cmd, rules, pos):
    # pos의 길이가 1보다 작으면 flag_rules에 해당하는 규칙 없음
    if len(pos) > 1:
        for i in range(len(pos)-1):
            cmd_type = cmd[pos[i]]
            # NULL일 경우 value값이 없음
            if rules.get(cmd_type) == 'NULL':
                continue
            else:
                cmd_value = cmd[pos[i]+1]
                # rules 규칙에 맞는지 확인
                if rules.get(cmd_type) == 'NUMBER':
                    for num in cmd_value:
                        if not num.isnumeric():
                            return False
                elif rules.get(cmd_type) == 'STRING':
                    for s in cmd_value:
                        if not s.isalpha():
                            return False
    else:
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

    # 주어진 rules을 확인하기 위해 rules라는 딕셔너리를 만든다.
    for rule in flag_rules:
        flag_name, flag_type = rule.split()
        rules[flag_name] = flag_type
    print(rules)

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