def lonely(couples):
    memory = couples[0]
    solo = [couples[0]]
    for i in couples:
        if memory != i:
            solo.append(i)
            memory = i
    return solo

# def lonely(couplse):
#     solo = [couplse[0]]
#     for i in couplse:
#         if solo[-1] == i:
#             continue
#         else:
#             solo.append(i)
#     return solo