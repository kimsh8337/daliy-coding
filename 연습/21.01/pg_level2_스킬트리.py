skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        check = 0
        for k in range(len(skill)-1):
            for j in range(check,len(skill_trees[i])):
                if skill_trees[i][j] in skill[k+1:]:
                    check = -1
                    break
                if skill[k] == skill_trees[i][j]:
                    if skill[k+1] in skill_trees[i][:j]:
                        check = -1
                        break
                    else:
                        check += 1
                        break
            if check == -1:
                break
        if check != -1:
            answer += 1

    return answer

print(solution(skill,skill_trees))