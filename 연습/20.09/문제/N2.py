# blocks = [[0,50], [0,22], [2,10], [1,4], [4,-13]]
blocks = [[0,92], [1,20], [2,11], [1,-81], [3,98]]

def solution(blocks):
    answer = []

    answer.append(blocks[0][1])

    for i in range(1,len(blocks)):
        num = 0
        if i == 1 or i == 2:
            st = i-1
            ed = st+i
            arr = []
            for j in range(st,ed):
                arr.append(answer[j])

        while(1):
            if blocks[i][0] == 0:
                answer.append(blocks[i][1])
                check = arr[num] - blocks[i][1]
                answer.append(check)
                num += 2
            elif blocks[i][0] == num:
                answer.append(blocks[i][1])
                check = arr[num-1] - blocks[i][1]
                if answer[ed+num-1] == 'a':
                    del answer[ed+num-1]
                    answer.insert(ed+num-1, check)
                num += 2
            if num > i and 'a' not in answer:
                arr=[]
                for j in range(ed, ed+1+i):
                    arr.append(answer[j])
                ed = ed+1+i
                break
            elif num > i+1 and 'a' in answer:
                index = 0
                for k in range(-1,-len(answer)+1,-1):
                    if answer[k] == 'a' and k == -1:
                        if answer[k-1] == 'a':
                            continue
                    if (answer[k] == 'a' and answer[k+1] != 'a') or (answer[k] == 'a' and answer[k-1] != 'a'):
                        index = k+len(answer)
                        break
                del answer[index]
                if len(answer) > index and answer[index] != 'a':
                    check = answer[index-i] - answer[index]
                    answer.insert(index, check)
                else:
                    check = answer[index-i-1] - answer[index-1]
                    answer.insert(index, check)
            else:
                answer.append('a')
                num += 1

    return answer

print(solution(blocks))