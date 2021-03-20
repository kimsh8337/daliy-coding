def solution(table, languages, preference):
    jobs,pre,score = [],[],[]
    lan = [[] for _ in range(len(table))]

    pos = 0
    for tab in table:
        ta = tab.split()
        jobs.append(ta[0])
        for i in range(len(lan),0,-1):
            lan[pos].append(ta[i])
        pos += 1

    for i in range(len(languages)):
        pre.append((languages[i],preference[i]))

    for i in range(len(lan)):
        res = 0
        for j in range(len(lan[i])):
            if lan[i][j] in languages:
                for k in range(len(pre)):
                    if lan[i][j] == pre[k][0]:
                        res += (j+1)*pre[k][1]
        score.append(res)

    if score.count(max(score)) > 1:
        a = []
        for i in range(len(score)):
            if score[i] == max(score):
                a.append(jobs[i])
        a.sort()
        ans = a[0]
    else:
        ans = jobs[score.index(max(score))]

    return ans

# print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
#                ["PYTHON", "C++", "SQL"],[7, 5, 5]))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
               ["JAVA", "JAVASCRIPT"],[7,5]))