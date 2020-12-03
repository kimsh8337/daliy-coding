k = 3
score = [24,22,20,10,5,3,2,1]

def soultion(k,score):
    answer = 0
    minus = [-1]
    arr = [-1]
    for i in range(1,len(score)):
        minus.append(score[i-1] - score[i])
        arr.append(score[i-1] - score[i])


    for i in range(1,len(minus)):
        num = 1
        for j in range(i+1,len(minus)):
            if minus[i] == minus[j]:
                num+=1

                if num >= k :
                    check = minus[i]

                    for z in range(1,len(minus)):
                        if arr[z] == check:
                            arr[z-1], arr[z] = 0, 0

    for i in range(len(arr)):
        if arr[i] != 0:
            answer += 1

    if answer == len(score):
        answer = 0
    return answer

print(soultion(k,score))