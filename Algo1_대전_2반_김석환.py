import sys
sys.stdin = open('input1.txt','r')

for tc in range(1,1+int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    change = [0]*10
    x = [0]*10


    for _ in range(n):
        # 절댓값이 10 이상일 경우
        for i in range(10):
            if abs(arr[i]) >= 10:
                if i == 0:
                    change[i] = -abs(arr[i])//2
                    # 이동 중 서로 영향을 주지 않기위해 그 자리에 값이 있을 경우, 새로운 배열 x에 값을 잠시 저장해둠.
                    if change[i+1] != 0:
                        x[i+1] = abs(arr[i])//2
                    else:
                        change[i+1] = abs(arr[i])//2
                if i == 9:
                    change[i] = abs(arr[i])//2
                    # 이동 중 서로 영향을 주지 않기위해 그 자리에 값이 있을 경우, 새로운 배열 x에 값을 잠시 저장해둠.
                    if change[i-1] != 0:
                        x[i-1] = -abs(arr[i])//2
                    else:
                        change[i-1] = -abs(arr[i])//2
                if i != 0 and i != 9:
                    # 이동 중 서로 영향을 주지 않기위해 그 자리에 값이 있을 경우, 새로운 배열 x에 값을 잠시 저장해둠.
                    if change[i+1] != 0:
                        x[i+1] = abs(arr[i])//2
                    else:
                        change[i+1] = abs(arr[i])//2
                    # 이동 중 서로 영향을 주지 않기위해 그 자리에 값이 있을 경우, 새로운 배열 x에 값을 잠시 저장해둠.
                    if change[i-1] != 0:
                        x[i-1] = -abs(arr[i])//2
                    else:
                        change[i-1] = -abs(arr[i])//2


        # 중간 값 옮기기(절댓값 10보다 작을때)
        for i in range(1,9):
            if arr[i] == 0:
                continue
            if abs(arr[i]) < 10:
                if arr[i] > 0:
                    # 이동 중 서로 영향을 주지 않기위해 그 자리에 값이 있을 경우, 새로운 배열 x에 값을 잠시 저장해둠.
                    if change[i+1] != 0:
                        x[i+1] = arr[i]
                    else:
                        change[i+1] = arr[i]
                elif arr[i] < 0:
                    # 이동 중 서로 영향을 주지 않기위해 그 자리에 값이 있을 경우, 새로운 배열 x에 값을 잠시 저장해둠.
                    if change[i-1] != 0:
                        x[i-1] = arr[i]
                    else:
                        change[i-1] = arr[i]

        # 가장자리 값 바꾸기
        for i in range(0,10,9):
            if i == 0:
                if arr[i] > 0:
                    change[i+1] += arr[i]
                if arr[i] < 0:
                    if change[i] == 0:
                        change[i] = -arr[i]
                    # 이동 중 서로 영향을 주지 않기위해 그 자리에 값이 있을 경우, 새로운 배열 x에 값을 잠시 저장해둠.
                    else:
                        x[i] = -arr[i]
            if i == 9:
                if arr[i] < 0:
                    change[i-1] += arr[i]
                if arr[i] > 0:
                    if change[i] == 0:
                        change[i] = -arr[i]
                    # 이동 중 서로 영향을 주지 않기위해 그 자리에 값이 있을 경우, 새로운 배열 x에 값을 잠시 저장해둠.
                    else:
                        x[i] = -arr[i]

        # 저장한 값 더해서 change배열 완성해주기
        for i in range(10):
            change[i] += x[i]
            x[i] = 0

        # change를 arr로 다시 바꿔주고 초기화
        for i in range(10):
            arr[i] = change[i]
            change[i] = 0
            x[i] = 0

    print('#{}'.format(tc), end = ' ')
    for i in range(10):
        print(arr[i], end= ' ')
    print()