debts = [['Alex', 'Blake', '5'], ['Blake', 'Alex', '3'], ['Casey', 'Alex', '7'],['Casey', 'Alex', '4'], ['Casey', 'Alex', '2']]

def smallestNegativeBalance(debts):
    ans = {}
    res = []

    for i in range(len(debts)):
        ans[debts[i][0]] = 0

    for person in ans.keys():
        for j in range(len(debts)):
            borrower = debts[j][0]
            lender = debts[j][1]
            if person == borrower:
                ans[person] -= int(debts[j][2])
            elif person == lender:
                ans[person] += int(debts[j][2])
    print(min(ans.values()))

    if min(ans.values()) >= 0:
        res.append("Nobody has a negative balance")
        return res

    for amount in ans.items():
        if amount[1] == min(ans.values()):
            res.append(amount[0])

    if len(res) < 1:
        res.append("Nobody has a negative balance")
    else:
        res.sort()


    # ans = []
    # res = [[] for _ in range(len(debts))]
    # minus = [float('inf')]
    # check = []
    #
    # for i in range(len(debts)):
    #     person = debts[i][0]
    #     amount = 0
    #     if person in check:
    #         continue
    #     for j in range(len(debts)):
    #         borrower = debts[j][0]
    #         lender = debts[j][1]
    #         if person == borrower:
    #             amount -= int(debts[j][2])
    #             check.append(debts[j][0])
    #         elif person == lender:
    #             amount += int(debts[j][2])
    #     res[i].append(amount)
    #     if amount < 0 and amount <= minus[0]:
    #         minus[0] = amount
    #
    # for i in range(len(res)):
    #     if res[i] == minus:
    #         ans.append(debts[i][0])
    # if len(ans) < 1:
    #     ans.append("Nobody has a negative balance")
    # else:
    #     ans.sort()

    return res

print(smallestNegativeBalance(debts))