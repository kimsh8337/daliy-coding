T = int(input())
for i in range(T):
    quiz = list(map(str, input()))
    score = 0
    sum = 0
    for j in range(len(quiz)):
        if quiz[j] == 'X':
            score = 0
        else:
            score += 1
            sum += score
    print(sum)