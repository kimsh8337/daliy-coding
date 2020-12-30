card_numbers = ["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"]

def solution(card_numbers):
    answer = []
    check = []
    for i in range(len(card_numbers)):
        sub = card_numbers[i].split('-')
        ch = 0
        if len(sub) != 1:
            for j in range(len(sub)):
                if len(sub[j]) == 4:
                    ch = 1
                else:
                    ch = 0
                    break
        else:
            if len(card_numbers[i]) == 16:
                ch = 1
            else:
                ch = 0
        if ch == 1:
            check.append(i)
        # if (len(sub) == 1 or len(sub) == 4) and len(''.join(sub)) == 16:
        #     check.append(i)
        card_numbers[i] = ''.join(sub)

    # print(card_numbers)

    for i in range(len(card_numbers)):
        a = 0
        b = 0
        if i in check:
            for j in range(len(card_numbers[i])):
                if j % 2 == 0:
                    plus = int(card_numbers[i][j]) * 2
                    if plus / 10 >= 1:
                        plus = (plus // 10) + (plus % 10)
                    a += plus
                else:
                    b += int(card_numbers[i][j])
            sum = a + b
            # print(i, sum)
            if sum % 10 == 0:
                answer.append(1)
            else:
                answer.append(0)
        else:
            # print(i)
            answer.append(0)

    return answer

print(solution(card_numbers))