n = 3
customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]

def check(customers,ki,play):
    if 0 in play:
        for i in range(len(play)):
            if play[i] == 0:
                play[i] += 1
                break
    else:
        smonth = customers.split()[0][0]
        sday = customers.split()[0][1]
        shour = customers.split()[1][0]
        smin = customers.split()[1][1]
        dur = customers.split()[2]
        emin = smin + customers.split()[2]
        ehour = shour
        eday = sday
        emonth = smonth
        if emin + dur > 59:
            ehour += 1
            if ehour > 23:
                eday += 1
                if smonth == 1 or smonth == 3 or smonth






    print(date,stime,dur,etime)


def solution(n, customers):
    answer = 0
    ki = []
    for i in range(1,n+1):
        ki.append(0)
    play = ki
    print(ki)
    print(play)
    # for i in range(len(customers)):
    #     if i == 0:
    #         ki[0] += 1
    #     if
    check(customers[0],ki,play)
    return answer

print(solution(n,customers))