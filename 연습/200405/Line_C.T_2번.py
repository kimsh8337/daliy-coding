def solution(answer_sheet, sheets):
    cnt = 0
    lg = 0
    for i in range(len(sheets)):
        for j in range(len(answer_sheet)):
            if sheets[i][j] != answer_sheet[j]:
                for k in range(i,len(sheets)):
                    for p in range(j,len(answer_sheet)):
                        if sheets[i][j] == sheets[k][j]:
                            cnt += 1
                            if sheets[i][j] == sheets[k][p]:
                                lg += 1
                            break
    answer = cnt + lg**2
    return answer

print(solution("24551",["24553", "24553", "24553", "24553"]))