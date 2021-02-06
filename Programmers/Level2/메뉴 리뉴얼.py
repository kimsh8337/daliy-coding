orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

from itertools import combinations

def solution(orders, course):
    answer = []

    for co in course:
        temp = {}
        for i in range(len(orders)):
            for com in combinations(sorted(orders[i]), co):
                com = ''.join(com)
                cnt = 1
                if com in temp:
                    cnt = temp.get(com)+1
                temp[com] = cnt
        if len(temp) > 0:
            if max(temp.values()) < 2:
                continue
            else:
                maxcnt = [k for k,v in temp.items() if max(temp.values()) == v]
                for e in maxcnt:
                    answer.append(e)

    return sorted(answer)

print(solution(orders, course))