import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    x,y = map(int, input().split())
    cnt = 0
    jump = 0
    jump_list=[]

    for i in range(y-x+1):
        if i == 0:
            cnt += 1
            jump = 1
            jump_list.append(jump)
        else:
            if jump != y-x-1:
                jump += jump+1
                jump_list.append(jump)
                cnt += 1
                if jump > y-x-1:
                    jump -= jump_list[-2]
            else:
                cnt += 1
                break
    print(cnt)
